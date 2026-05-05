import os

MONTHS = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


PLATFORM_MEDIUM = "Medium"
PLATFORM_DEV_TO = "dev.to"


MEDIUM_BASE_URL = "https://api.medium.com/v1/"
MEDIUM_USER_ID = os.environ.get("MEDIUM_USER_ID")
MEDIUM_TOKEN = os.environ.get("MEDIUM_TOKEN")
PERSONAL_WEBSITE = "https://www.abhin.dev/"

CLOUDINARY_CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.environ.get("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.environ.get("CLOUDINARY_API_SECRET")
