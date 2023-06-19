from PythonProject.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print("In Preflight Step")
        utils.create_dir()
