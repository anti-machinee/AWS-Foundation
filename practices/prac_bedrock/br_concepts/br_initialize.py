import os
import boto3

name_profile = os.getenv('AWS_PROFILE')
aws_session = boto3.session.Session(profile_name=name_profile)
bedrock = boto3.client('bedrock')
bedrock_runtime = boto3.client('bedrock-runtime')