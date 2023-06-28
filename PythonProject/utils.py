import os

from PythonProject.settings import DOWNLOADS_DIR, URLS_DIR, CAPTIONS_DIR


def get_video_id(url):
    return url.split("watch?v=")[-1]


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(URLS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    @staticmethod
    def get_video_id(url):
        return url.split("watch?v=")[-1]

    @staticmethod
    def get_url_file(channel_id):
        return os.path.join(URLS_DIR, channel_id + ".txt")


