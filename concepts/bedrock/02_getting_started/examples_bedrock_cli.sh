aws bedrock list-foundation-models --region us-east-1

aws bedrock-runtime invoke-model \
--model-id amazon.titan-text-express-v1 \
--body '{"inputText": "Describe what is a good student", "textGenerationConfig" : {"maxTokenCount": 512, "temperature": 0.5, "topP": 0.9}}' \
--cli-binary-format raw-in-base64-out \
invoke-model-output-text.txt

# update AWS CLI if current AWS CLI version does not support converse
aws bedrock-runtime converse \
--model-id amazon.titan-text-express-v1 \
--messages '[{"role": "user", "content": [{"text": "Describe what is a good student"}]}]' \
--inference-config '{"maxTokens": 512, "temperature": 0.5, "topP": 0.9}'
