from sm_pipeline.steps.step_process import StepProcess
from sm_pipeline.steps.step_train import StepTrain
from sm_pipeline.steps.step_evaluate import StepEvaluate
from sm_pipeline.steps.step_condition import StepCondition


step_registry = {
    "process": StepProcess,
    "train": StepTrain,
    "evaluate": StepEvaluate,
    "condition": StepCondition,
}