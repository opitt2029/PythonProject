import os

import yt_dlp

from PythonProject.pipeline.steps.step import Step
from PythonProject.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print(os.path.join(os.getcwd(), utils.get_caption_path(url)))
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': os.path.join(os.getcwd(), utils.get_caption_path(url))
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
