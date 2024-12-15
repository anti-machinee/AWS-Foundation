# Amazon Bedrock foundation model information
- Usages with FMs
    - Run inference
    - Evaluate models
    - Set up knowledge bases
    - Create an agent
    - Customize a model
    - Purchase provisioned throughput

# Get information about foundation models
- Retrieve information about FMs

# Supported foundation models in Amazon Bedrock
- Acknowledge about providers supported by AWS
- For each model, acknowledge about these categories
    - Model ID
    - Region supported
    - Input modalities
    - Output modalities
    - Streaming supported
    - Inference parameters

# Model support by AWS Region in Amazon Bedrock
- Models are not always supported in regions
- Models are accessible via cross region inference

# Feature support by AWS Region in Amazon Bedrock
- These features supports are different between regions
    - Agents
    - IDE
    - Application inference profiles
    - Batch inference
    - Continued pre-training
    - Custom model import
    - Fine tuning
    - Flows
    - Guardrails
    - Knowledge bases
    - Latency optimization
    - Model evaluation
    - Prompt management
    - Prompt optimization
    - Provisioned throughput
    - RAG evaluations
    - Rerank

# Model support by feature
- Features above can be supported differently by models
- A model does not always support these features

# Inference request parameters and response fields for foundation models
- To call API correctly, follow identical format of each model
- If customize base models, still follow formats of base models
- If use parameters not match formats, these parameters are ignored

# Custom model hyperparameters
- Control training processes
- These hyperparameters
    - Epochs
    - Batch size
    - Learning rate
    - Learning rate warmup steps
    - Steps
    - Learning rate multipliers
    - Early stopping threshold
