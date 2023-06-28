import os
import urllib.request
import json

from PythonProject.settings import URLS_DIR
from PythonProject.pipeline.steps.step import Step
from PythonProject.settings import API_KEY


class GetVideoList(Step):
    def process(self, datas, inputs, utils):
        channel_id = inputs["channel_id"]
        api_key = API_KEY
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)
        video_links = []
        url = first_url

        count = 0

        url_file_path = utils.get_url_file(inputs["channel_id"])
        url_files_location = os.path.join(os.getcwd(), url_file_path)

        if os.path.exists(url_files_location) and os.path.getsize(url_files_location) > 0:
            print("Found existing video list file for channel_id: ", channel_id)
            return self.read_file(url_files_location)

        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                count += 1
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break

        print(f"Total links: {count}")

        self.write_file(url_files_location, video_links)
        datas = video_links

        return datas

    @staticmethod
    def read_file(file_path):
        with open(file_path, "r") as file:
            video_links = []
            for url in file:
                video_links.append(url.strip())
        return video_links

    @staticmethod
    def write_file(file_path, datas):
        count = 0
        target = len(datas)
        with open(file_path, "w") as file:
            for url in datas:
                count += 1
                if count != target:
                    file.write(url + ",\n")
                else:
                    file.write(url)
