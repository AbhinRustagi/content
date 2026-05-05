import os

import yaml

from lib import Post, process_images_in_posts


def parse_markdown(file_path):
    '''Parse a markdown file and return the metadata and HTML content.'''
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        end_metadata = content.find('---', 3)
        metadata_raw = content[3:end_metadata].strip()
        markdown_content = content[end_metadata+3:].strip()
        metadata = yaml.safe_load(metadata_raw)
    else:
        metadata = {}
        markdown_content = content

    return metadata, markdown_content


def discover_posts(directory):
    '''Walk posts/<year>/<month>/*.md and return a flat list of Post objects.'''
    posts = []
    for year in os.listdir(directory):
        year_dir = os.path.join(directory, year)
        if not os.path.isdir(year_dir):
            continue
        for month in os.listdir(year_dir):
            month_dir = os.path.join(year_dir, month)
            if not os.path.isdir(month_dir):
                continue
            for post_file in os.listdir(month_dir):
                path = os.path.join(month_dir, post_file)
                frontmatter, content = parse_markdown(path)
                frontmatter["path"] = path
                posts.append(Post(frontmatter, content))
    return posts


def publish_new_posts(unpublished):
    for post in unpublished:
        print(f"New post found: {post.title}")
        post.publish()


def main():
    '''Discover posts, upload images to Cloudinary, publish new posts to Medium.

    Index.json and README.md are managed by the repo-db-indexer GitHub Action.
    '''
    posts = discover_posts("posts")
    process_images_in_posts(posts)

    unpublished = [post for post in posts if not post.published]
    if unpublished:
        print(f"Found {len(unpublished)} unpublished posts.")
        publish_new_posts(unpublished)


main()
