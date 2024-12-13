# https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
 
BODY_TITAN = {
    "inputText": None, 
    "textGenerationConfig": {
        "temperature":0.2,
        "topP":0.95, 
        "maxTokenCount": 200,
    }
}

BODY_TITAN_EMBED = {
    "inputText": None,
    # "dimensions": 1024,
    # "normalize": True,
    # "embeddingTypes": ["float"]
}

BODY_STABILITY = {
    "text_prompts": [
        {
            "text": None
        }
    ],
    "cfg_scale": 10,
    "seed": 20,
    "steps": 50
}

BODY_CLAUDE = {
    "anthropic_version": "bedrock-2023-05-31", 
    "max_tokens": int(500/0.75),
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": None
                }
            ]
        }
    ]
}