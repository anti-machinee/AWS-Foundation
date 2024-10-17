# Guidance for Conversational Chatbots using Retrieval Augmented Generation (RAG) on AWS
Note: This sample is not implemented in AWS. Document and source code are based on assumptions and references

# Introduction
- This sample is analysis of the [1]
- This sample is for understanding RAG with AWS in high level

# Analysis

## Usage case
- A QA application provides retrieval augmented generation (RAG) for querying

## User stories
- This application provides data query service
- This application uses RAG for querying
- This application use OpenSearch for data store
- Use Python CDK for infrastructure as code

## Solutions
### Target data store
- Raw data is stored in S3
- Then using SageMaker to transform from documents to embeddings and store in OpenSearch
### Query orchestration
- Queries is executed via Streamlit web application
- LLM is hosted on AWS SageMaker endpoint
- Context retrieved is used to form a prompt for the LLM

## Architecture and workflow
![RAG Architecture](assets/rag_with_opensearch_arch.svg?raw=true "RAG with Amazon Kendra")
- See [1] for more details

## Guideline in detail

### Step 1: Infrastructure
- Infrastructure as code using Python CDK
- Prepare 
    - cdk.json: define setting of CDK
    - app.py: aws cdk client to creates stacks
#### Stack
- RAGVpcStack
    - Create CDK stack in existing VPC or create new VPC
    - If new VPC, provide CIDR (private and public), gateway, subnet, etc.
- RAGOpenSearchStack
    - Create secret for OpenSearch
    - Create OpenSearch domain
- RAGSageMakerStudioStack
    - Sets up a complete SageMaker Studio environment with the necessary permissions for various AWS services, including S3, OpenSearch, and SecretsManager
    - Configures user settings for JupyterLab within SageMaker Studio and integrates the necessary policies for Docker image building via CodeBuild.
- EmbeddingEndpointStack
    - Create SageMaker endpoint for LLM embedding
- LLMEndpointStack
    - Create SageMaker endpoint for LLM
- StreamlitAppStack
    - Deploys a Streamlit application on AWS ECS using Fargate
    - Utilizes IAM roles for secure access to AWS resources like Secrets Manager and SageMaker endpoints
    - Configures networking with a security group and a load balancer for public access

### Step 2: Query orchestration
#### Ingest data to OpenSearch
- Create a SageMaker processing job
    - Parallel loading
        - Duplicate ECR
    - Sequential loading
    - Add documents to OpenSearch
- Search similar documents
    - Use OpenSearchVectorSearch

### Step 3: User interface
- Run the Streamlit web application for the question answering bot
    - Hand on Streamlit and conversational chatbot

# Implementation
- See [1] for more details

# References
- [1] https://github.com/aws-samples/rag-with-amazon-opensearch-and-sagemaker/tree/main