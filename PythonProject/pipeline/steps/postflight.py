from PythonProject.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print("In Postflight Step")
