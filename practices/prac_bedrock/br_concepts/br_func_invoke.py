import json
import base64
import io
from PIL import Image
from IPython.display import display_markdown, Markdown

from br_initialize import *
from br_body import *


def invoke_model_titan(
    model_id,
    accept,
    content_type,
    text
):
    body0 = BODY_TITAN
    body0["inputText"] = text
    body = json.dumps(body0)
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = json.loads(response.get("body").read())
    output_text = response_body.get("results")[0].get("outputText")
    print(response)
    print(response_body)
    print(output_text)


def invoke_stream_model_titan(
    model_id,
    accept,
    content_type,
    text
):
    body0 = BODY_TITAN
    body0["inputText"] = text
    body = json.dumps(body0)
    response = bedrock_runtime.invoke_model_with_response_stream(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = response.get("body")
    
    output = []
    if response_body:
        for event in response_body:
            chunk = event.get('chunk')
            if chunk:
                chunk_obj = json.loads(chunk.get('bytes').decode())
                text = chunk_obj['outputText']
                output.append(text)
                display_markdown(Markdown(print(text, end='')))
    print(output)


def invoke_stream_model_claude(
    model_id,
    accept,
    content_type,
    text
):
    body0 = BODY_CLAUDE
    body0["messages"][0]["content"][0]["text"] = text
    body = json.dumps(body0)
    response = bedrock_runtime.invoke_model_with_response_stream(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = response.get("body")
    
    output = []
    if response_body:
        for event in response_body:
            chunk = event.get('chunk')
            if chunk:
                chunk_obj = json.loads(chunk.get('bytes').decode())
                if 'delta' in chunk_obj:
                    delta_obj = chunk_obj.get('delta', None)
                    if delta_obj:
                        text = delta_obj.get('text', None)
                        print(text, end='')
                        if not text :
                            break
                    output.append(text[0]) if type(text) is list and len(text) > 0 else output.append(text)
                    display_markdown(Markdown(print(text, end='')))
    print(output)


def invoke_model_titan_embed(
    model_id,
    accept,
    content_type,
    text
):
    body0 = BODY_TITAN_EMBED
    body0["inputText"] = text
    body = json.dumps(body0)
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = json.loads(response.get("body").read())
    embedding = response_body.get("embedding")
    print(response)
    print(response_body)
    print(embedding)
    print(len(embedding))


def invoke_model_stability(
    model_id,
    accept,
    content_type,
    text
):
    body0 = BODY_STABILITY
    body0["text_prompts"][0]["text"] = text
    body = json.dumps(body0)
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = json.loads(response.get("body").read())
    data_base64 = response_body.get("artifacts")[0].get("base64")
    image = Image.open(io.BytesIO(base64.decodebytes(bytes(data_base64, "utf-8"))))
    print(response)
    print(response_body)
    print(data_base64)
    image.show()


if __name__ == '__main__':
    # invoke_model_titan(
    #     model_id="amazon.titan-tg1-large",
    #     accept="application/json",
    #     content_type="application/json",
    #     text="Hello world"
    # )

    # invoke_stream_model_titan(
    #     model_id="amazon.titan-tg1-large",
    #     accept="application/json",
    #     content_type="application/json",
    #     text="Generate an short essay"
    # )

    # invoke_stream_model_claude(
    #     model_id="anthropic.claude-3-haiku-20240307-v1:0",
    #     accept="application/json",
    #     content_type="application/json",
    #     text="Generate an short essay"
    # )

    invoke_model_titan_embed(
        model_id="amazon.titan-embed-g1-text-02",
        accept="application/json",
        content_type="application/json",
        text="This text will be embedded"
    )

    # invoke_model_stability(
    #     model_id="stability.stable-diffusion-xl-v1",
    #     accept="application/json",
    #     content_type="application/json",
    #     text="A man with a hat"
    # )