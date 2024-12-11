from sm_pipeline.get_step import step_registry


class SMPipeline:
    def __init__(
        self,
        config
    ):
        self.cfg = config
        self.steps = self.prepare_steps()

    def set_step(self, name_step, config_step):
        step_type = config_step.type
        step = step_registry[step_type](name_step, config_step).get_step()
        return step

    def prepare_steps(self):
        list_steps = {}
        for step in self.cfg.steps:
            list_steps[step.name] = self.set_step(step.name, step.args[0])
        return list_steps

    def create_pipeline(self):
        pass
