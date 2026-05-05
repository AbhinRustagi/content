import os
import re

import cloudinary
import cloudinary.uploader

from .utils import CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, CLOUDINARY_CLOUD_NAME


def configure_cloudinary():
    """Configure cloudinary with credentials. Returns False if credentials are missing."""
    if not all([CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET]):
        print("Cloudinary credentials not configured, skipping image upload")
        return False

    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_API_KEY,
        api_secret=CLOUDINARY_API_SECRET
    )
    return True


def extract_local_images(content):
    """Extract local image paths from markdown content"""
    pattern = r'!\[.*?\]\((/images/[^)]+)\)'
    return re.findall(pattern, content)


def upload_image(local_path):
    """Upload image to Cloudinary and return the URL"""
    full_path = local_path.lstrip('/')
    if not os.path.exists(full_path):
        print(f"Image not found: {full_path}")
        return None

    result = cloudinary.uploader.upload(full_path, folder="blog")
    print(f"Uploaded {full_path} to Cloudinary: {result.get('secure_url')}")
    return result.get('secure_url')


def replace_image_urls(content, url_mapping):
    """Replace local image paths with Cloudinary URLs"""
    for local_path, cloudinary_url in url_mapping.items():
        content = content.replace(local_path, cloudinary_url)
    return content


def delete_local_image(local_path):
    """Delete local image file"""
    full_path = local_path.lstrip('/')
    if os.path.exists(full_path):
        os.remove(full_path)
        print(f"Deleted local image: {full_path}")


def process_images_in_posts(posts):
    """Process all images in all posts - upload to Cloudinary and update content"""
    if not configure_cloudinary():
        return

    images_to_upload = set()
    for post in posts:
        local_images = extract_local_images(post.content)
        images_to_upload.update(local_images)

    if not images_to_upload:
        print("No local images found to upload")
        return

    print(f"Found {len(images_to_upload)} local images to upload")

    url_mapping = {}
    for local_path in images_to_upload:
        cloudinary_url = upload_image(local_path)
        if cloudinary_url:
            url_mapping[local_path] = cloudinary_url
            delete_local_image(local_path)

    for post in posts:
        if any(path in post.content for path in url_mapping.keys()):
            post.content = replace_image_urls(post.content, url_mapping)
            post.save()
            print(f"Updated image URLs in: {post.path}")
