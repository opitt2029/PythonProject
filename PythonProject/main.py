from PythonProject.utils import Utils
from PythonProject.pipeline.steps.prefilght import Preflight
from PythonProject.pipeline.pipeline import Pipeline
from PythonProject.pipeline.steps.get_video_list import GetVideoList
from PythonProject.pipeline.steps.download_captions import DownloadCaptions
from PythonProject.pipeline.steps.postflight import Postflight


def main():
    user_inputs = {
        "channel_id": "UCKSVUHI9rbbkXhvAXK-2uxA"
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight()
    ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(user_inputs, utils)


if __name__ == "__main__":
    main()
