import json

import boto3
from botocore.exceptions import ClientError


def list_models():
    bedrock = boto3.client(
        service_name="bedrock"
    )
    models = bedrock.list_foundation_models()
    print(models)


def submit_text_by_invoke():
    brt = boto3.client("bedrock-runtime")
    model_id = "amazon.titan-text-express-v1"
    prompt = "Describe a good student"
    native_request = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0.5,
            "topP": 0.9
        },
    }
    request = json.dumps(native_request)
    try:
        response = brt.invoke_model(modelId=model_id, body=request)
    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)
    model_response = json.loads(response["body"].read())
    response_text = model_response["results"][0]["outputText"]
    print(response_text)


def submit_text_by_converse():
    brt = boto3.client("bedrock-runtime")
    model_id = "amazon.titan-text-express-v1"
    user_message = "Describe a good student"
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]
    try:
        response = brt.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )
        response_text = response["output"]["message"]["content"][0]["text"]
        print(response_text)
    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)


if __name__ == "__main__":
    list_models()
    submit_text_by_invoke()
    submit_text_by_converse()
