import boto3
import json


def sample_1():
    brt = boto3.client(service_name='bedrock-runtime')
    body = json.dumps({
        "prompt": "\n\nHuman: Explain what is a good student\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })
    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    print(response_body.get('completion'))


def sample_2():
    brt = boto3.client(service_name='bedrock-runtime')
    body = json.dumps({
        'prompt': '\n\nHuman: Explain what is a good student\n\nAssistant:',
        'max_tokens_to_sample': 4000
    })
    response = brt.invoke_model_with_response_stream(
        modelId='anthropic.claude-v2', 
        body=body
    )
    stream = response.get('body')
    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                print(json.loads(chunk.get('bytes').decode()))


if __name__ == '__main__':
    sample_1()
    sample_2()
