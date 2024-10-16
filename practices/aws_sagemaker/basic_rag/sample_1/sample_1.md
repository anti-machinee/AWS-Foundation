# Guidance for Conversational Chatbots using Retrieval Augmented Generation (RAG) on AWS
Note: This sample is not implemented in AWS. Document and source code are based on assumptions and references

# Introduction
- This sample is re-implementation of the [1]

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
#### Data store
- Kendra
    - DocsKendraIndex
    - KendraDocsDS
- Custom
    - DataSourceSync
- DynamoDB
    - ConversationHistory
#### Compute resources
- Lambda
    - DataSourceSyncLambda
    - LambdaFunction
    - LexLambdaPermission
    - LambdaLayer
- SageMaker
    - LLMModel
    - LLMEndpointConfig
    - LLMEndpoint
#### User interface
- Lex
    - KendraLLMRAGBot

### Step 2: Target data store
### Step 3: Query orchestration
### Step 4: Conversational memory store
### Step 5: User interface
### Step 6: Deployment

# Implementation
- See [1] for more details

# References
- [1] https://github.com/aws-solutions-library-samples/guidance-for-conversational-chatbots-using-retrieval-augmented-generation-on-aws
- [2] https://aws.amazon.com/solutions/guidance/conversational-chatbots-using-retrieval-augmented-generation-on-aws/