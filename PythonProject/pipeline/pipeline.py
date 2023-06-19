from PythonProject.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)

            except StepException as err:
                print(f"Exception happened in {step} step!!\ncontent: {err}")
                break
