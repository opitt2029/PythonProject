import os
import time

import yt_dlp

from PythonProject.pipeline.steps.step import Step
from PythonProject.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        url_file_path = utils.get_url_file(inputs["channel_id"])

        if os.path.exists(url_file_path) and os.path.getsize(url_file_path) > 0:
            print(f"The video list of channle id: {inputs['channel_id']} already exists.")
            with open(url_file_path, "r") as links:
                data = []
                for link in links:
                    data.append(links.readline())

        for url in data:

            caption_file_name = os.path.join(inputs["channel_id"], utils.get_video_id(url))
            captions_file_path = os.path.join(os.getcwd(), CAPTIONS_DIR, caption_file_name)
            captions_file_path = captions_file_path.strip()
            print("\n\n", captions_file_path)

            ydl_opts = {
                'download_archive': captions_file_path,
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': captions_file_path,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        end = time.time()
        print("Took", end - start, "seconds")

        