import json
import pandas as pd

import sagemaker, boto3
from sagemaker.jumpstart import JumpStartModel
from sagemaker.jumpstart.estimator import JumpStartEstimator
from sagemaker.serializers import JSONSerializer


class Configuration:
    def __init___(self):
        pass

    def get_role(self):
        role = sagemaker.get_execution_role()
        return role
    
    def create_session(self):
        sess = sagemaker.Session()
        return sess
    

def get_dataset(
    output_bucket,
    output_prefix
):
    s3 = boto3.client('s3')

    bucket_name = 'jumpstart-cache-prod-us-west-2'
    file_key = 'training-datasets/Amazon_SageMaker_FAQs/Amazon_SageMaker_FAQs.csv'
    local_file_name = 'Amazon_SageMaker_FAQs.csv'
    s3.download_file(bucket_name, file_key, local_file_name)

    data = pd.read_csv(local_file_name, names=["Questions", "Answers"])
    data["id"] = data.index
    data_req = data[["id", "Answers"]]
    local_file = 'data.csv'
    data_req.to_csv(local_file, index=False, header=False)

    
    s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"
    training_dataset_s3_path = f"s3://{output_bucket}/{output_prefix}/data/data.csv"
    s3.upload_file(local_file, training_dataset_s3_path)
    
    return s3_output_location


def get_predictor(
    model_id: str,
    initial_instance_count: int, 
    instance_type: str
):
    model = JumpStartModel(
        model_id=model_id
    )
    predictor_llm = model.deploy(
        initial_instance_count=initial_instance_count, 
        instance_type=instance_type
    )
    return predictor_llm


def get_predictor_nn(
    model_id: str,
    output_bucket: str,
    output_prefix: str,
    s3_output_location
):
    hyperparameters = sagemaker.hyperparameters.retrieve_default(
        model_id=model_id, 
        model_version="*"
    )
    hyperparameters["batch_size"] = "64"

    estimator = JumpStartEstimator(
        model_id=model_id, 
        hyperparameters=hyperparameters, 
        output_path=s3_output_location
    )
    estimator.fit({"training": f"s3://{output_bucket}/{output_prefix}/data"}, logs=True)

    predictor_nn = estimator.deploy()
    
    return predictor_nn


def form_request(
    predictor_nn,
    question,
    top_k
):
    predictor_nn.serializer = JSONSerializer()
    predictor_nn.content_type = "application/json"
    payload_nearest_neighbour = {
        "queries": [question],
        "top_k": top_k,
        "mode": "nn_train_data",
        "return_text": True,
    }
    return payload_nearest_neighbour


def form_response(
    question,
    answer,
    newline="\n"
):
    response_message = f"The input Question is: {question}{newline} The Corresponding Answer is: {answer}"
    return response_message


def run_inference(
    predictor_nn,
    payload_nearest_neighbour
):
    predictor_nn.serializer = JSONSerializer()
    predictor_nn.content_type = "application/json"
    response = predictor_nn.predict(payload_nearest_neighbour)
    answer = response[0][0]["text"]
    return answer


def construct_context(
    contexts,
    max_section_len=1000,
    separator="\n",
):
    chosen_sections = []
    chosen_sections_len = 0

    for text in contexts:
        text = text.strip()
        # Add contexts until we run out of space.
        chosen_sections_len += len(text) + 2
        if chosen_sections_len > max_section_len:
            break
        chosen_sections.append(text)
    concatenated_doc = separator.join(chosen_sections)
    return concatenated_doc


def create_payload(question, context_str) -> dict:
    prompt_template = """Answer the following QUESTION based on the CONTEXT
    given. If you do not know the answer and the CONTEXT doesn't
    contain the answer truthfully say "I don't know".

    CONTEXT:
    {context}


    ANSWER:
    """

    text_input = prompt_template.replace("{context}", context_str).replace("{question}", question)

    payload = {
        "inputs": [
            [
                {"role": "system", "content": text_input},
                {"role": "user", "content": question},
            ]
        ],
        "parameters": {
            "max_new_tokens": 256,
            "top_p": 0.9,
            "temperature": 0.6,
            "return_full_text": False,
        },
    }
    return payload


def main():
    config = Configuration()
    sess = config.create_session()

    output_bucket = sess.default_bucket()
    output_prefix = "jumpstart-example-ss-training"

    filepath_out = get_dataset(
        output_bucket=output_bucket,
        output_prefix=output_prefix,
    )

    predictor = get_predictor(
        model_id="meta-textgeneration-llama-2-7b-f",
        initial_instance_count=1,
        instance_type="ml.g5.4xlarge"
    )

    predictor_nn = get_predictor_nn(
        model_id="huggingface-sentencesimilarity-gte-small",
        output_bucket=output_bucket,
        output_prefix=output_prefix,
        s3_output_location=filepath_out
    )

    question = "Is R supported with Amazon SageMaker?"
    
    request = form_request(
        predictor_nn,
        question,
        top_k=1
    )

    answer = run_inference(
        predictor_nn,
        request
    )

    response = form_response(
        question,
        answer
    )

    contexts = [ans["text"] for ans in response]

    context_str = construct_context(contexts=contexts)
    
    payload = create_payload(question, context_str)
    
    out = predictor.predict(payload, custom_attributes="accept_eula=true")
    generated_text = out[0]["generation"]["content"]

    return generated_text


if __name__ == "__main__":
    main()
