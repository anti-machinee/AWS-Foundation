import boto3 

bedrock = boto3.client(service_name='bedrock')
bedrock.list_foundation_models()
bedrock.get_foundation_model(modelIdentifier='anthropic.claude-v2')
