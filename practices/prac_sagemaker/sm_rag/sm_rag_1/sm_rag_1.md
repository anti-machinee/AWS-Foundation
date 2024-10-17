# Guidance for Conversational Chatbots using Retrieval Augmented Generation (RAG) on AWS
Note: This sample is not implemented in AWS. Document and source code are based on assumptions and references

# Introduction
- This sample is analysis of the [1]
- This sample is for understanding RAG with AWS in high level

# Analysis

## Usage case
- A conversational chabot providing private queries for a financial company

## User stories
- This application provides data query service
- This application uses RAG for querying
- This application bases on AWS services

## Solutions
### Target data store
- Target data is stored in AWS Kendra data source
### Query orchestration
- Queries is executed by AWS Lambda function
- Query orchestration is executed by LangChain
- LLM is hosted on AWS SageMaker endpoint
### Conversational memory store
- Conversational memory is stored in AWS DynamoDB
### User interface
- User interface is provided by AWS Lex

## Architecture and workflow
![RAG Architecture](assets/RAG_Kendra.png?raw=true "RAG with Amazon Kendra")
- See [1] for more details

## Guideline in detail

### Step 1: Infrastructure
#### IAM roles
- IAM roles
    - Common
        - Resources are in specific region and account using !Ref
        - Policies are named using !Join
        - Roles are named using !Join
    - KendraIndexRole
        - Assume role
            - Allow Kendra to assume this role using STS
        - Policies
            - Allow Kendra push metrics to CloudWatch only in Kendra namespace
            - Allow Kendra list all log groups in CloudWatch
            - Allow Kendra create log groups in CloudWatch. Generate dynamically ARN for log groups belong to Kendra
            - Allow Kendra describe/create/put log streams in CloudWatch. Generate dynamically ARN for log streams belong to Kendra
    - KendraDSRole
        - Assume role
            - Allow Kendra to assume this role using STS
        - Policies
            - Allow Kendra to batch put/delete documents in DocsKendraIndex index. Generate dynamically ARN for Kendra index
    - DataSourceSyncLambdaRole
        - Assume role
            - Allow Lambda to assume this role using STS
        - Policies
            - Attach default policies 
                AWSLambdaBasicExecutionRole
            - Allow Lambda to start data source sync job in Kendra. Generate dynamically ARN for Kendra index
    - LambdaIAMRole
        - Assume role
            - Allow Lambda to assume this role using STS
        - Policies
            - Attach default policies 
                AWSLambdaBasicExecutionRole
                AmazonS3FullAccess
    - SagemakerIAMRole
        - Assume role
            - Allow SageMaker to assume this role using STS
        - Policies
            - Attach default policies 
                AmazonSageMakerFullAccess
    - LexBotIAMRole
        - Assume role
            - Allow Lex to assume this role using STS
        - Policies
            - Allow Lex to invoke Lambda function. Only for LambdaFunction
    - BotRuntimeRole
        - Assume role
            - Allow Lex to assume this role using STS
        - Policies
            - Allow Lex to do SynthesizeSpeech and DetectSentiment
- IAM policies
    - LambdaExecutionPolicy
        - Allow Lambda function do InvokeEndpoint with Sagemaker
        - Allow Lambda function do BatchQuery, Query with Kendra
        - Allow some actions with DynamoDB
#### Data store
- Kendra
    - DocsKendraIndex
        - Get RoleArn from KendraIndexRole 
    - KendraDocsDS
        - Attach with DocsKendraIndex
        - Setup DataSourceConfiguration
        - Get RoleArn from KendraDSRole
- Custom
    - DataSourceSync
        - Use ServiceToken to link to LambdaFunction
- DynamoDB
    - ConversationHistory
#### Compute resources
- Lambda
    - DataSourceSyncLambda
        - Get RoleArn from DataSourceSyncLambdaRole
        - Handle to ensure Kendra index is kept up to date with data source
        - Source code is stored in Zipfile
    - LambdaFunction
        - Get RoleArn from LambdaIAMRole
        - Handle to do orchestration between Kendra, Sagemaker and Lex
        - Source code is stored in S3
    - LexLambdaPermission
        - Allow Lex to invoke Lambda function
    - LambdaLayer
        - Allow users to package/share libraries, runtimes and other dependencies between Lambda function
        - Source code is stored in S3
- SageMaker
    - LLMModel
        - Model data is stored in S3
        - Model is executed in Docker ECR
    - LLMEndpointConfig
        - Configure endpoint for LLMModel instance count/type, variant weight
        - Add cfn_nag for security check
    - LLMEndpoint
        - Create endpoint for LLMModel
#### User interface
- Lex
    - KendraLLMRAGBot
        - Get RoleArn from BotRuntimeRole
        - Secure data privacy
        - Setup code hook for Lambda function
        - Check NLU for intent
        - Set intents greeting and fallback intent
        - Setup locale and voice

### Step 2: Query orchestration
- Lambda function is trigger given an event
- Event stores information of intent name
- Check and mapping intent with intent handlers
- Hello/Goodbye/Fallback/Standard intents are supported
- For standard and fallback intents, there is an AI handler
- In AI handler, there is a query orchestration
    - Initialize LLM for text generation
    - Initialize Kendra tool for data searching
    - Initialize DynamoDB for conversational memory
- Finally, AI handler run LangChain orchestrate

# Implementation
- See [1] for more details

# References
- [1] https://github.com/aws-solutions-library-samples/guidance-for-conversational-chatbots-using-retrieval-augmented-generation-on-aws
- [2] https://aws.amazon.com/solutions/guidance/conversational-chatbots-using-retrieval-augmented-generation-on-aws/