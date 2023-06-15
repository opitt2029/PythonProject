from PythonProject.pipeline.pipeline import Pipeline
from PythonProject.pipeline.steps.get_video_list import GetVideoList


def main():
    user_inputs = {
        "channel_id": "UCKSVUHI9rbbkXhvAXK-2uxA"
    }

    steps = [
        GetVideoList(),
            ]

    p = Pipeline(steps)
    p.run(user_inputs)


if __name__ == "__main__":
    main()
