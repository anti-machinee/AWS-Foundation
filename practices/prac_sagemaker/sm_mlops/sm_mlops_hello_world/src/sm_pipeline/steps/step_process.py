from multiprocessing import process
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep


class StepProcess:
    def __init__(
        self,
        name_step,
        config_step
    ):  
        self.name = name_step
        self.cfg = config_step

    def set_processor(self):
        processor = SKLearnProcessor(
            framework_version=sklearn_framework_version,
            instance_type="ml.m5.large",
            instance_count=processing_instance_count,
            base_job_name="sklearn-housing-data-process",
            role=role,
            sagemaker_session=pipeline_session,
        )
        return processor

    def set_arguments(self):
        processor = self.set_processor()
        arguments = processor.run(
            inputs=[
                ProcessingInput(source=input_data, destination="/opt/ml/processing/input"),
            ],
            outputs=[
                ProcessingOutput(output_name="scaler_model", source="/opt/ml/processing/scaler_model"),
                ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
                ProcessingOutput(output_name="test", source="/opt/ml/processing/test"),
            ],
            code="code/preprocess.py",
        )
        return arguments

    def set_step(self):
        arguments = self.set_arguments()
        step = ProcessingStep(
            name=self.name,
            step_args=arguments
        )
        return step

