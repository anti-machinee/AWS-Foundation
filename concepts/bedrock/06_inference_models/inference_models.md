# Submit prompts and generate responses with model inference
- Inputs
    - Prompt
    - Model
    - Parameters
- Output
    - Text
    - Image
    - Embeddings
- Inference by
    - Console
    - Converse or invoke models
    - Batch inference
- Inference supports other tasks
    - Model evaluation
    - Knowledge bases
    - Agents
    - Flows

# Influence response generation with inference parameters
- Factors are influenced
    - Randomness and diversity
        - Temperature: impact randomness. As high temperature as high random
        - Top K: impact diversity. As high top K as high diversity
        - Top P: impact deterministic. As high top P as high diversity
    - Length
        - Response length
        - Penalties
        - Stop sequences

# Supported Regions and models for running model inference
- Not all models and all features are supported in a region

# Prerequisites for running model inference
- Support authorization
    - Actions
    - Resource types
    - Condition
- Understand these roles help understand what AWS provides and how these roles impact to supported features

# Generate responses in the console using playgrounds
- Use PG to test model to decide suitable models
- Equivalent to making API calls
- Support
    - Chat/text
        - Chat: sequences of rounds
        - Single prompt
    - Image
        - Submit text prompt to generate an image
- Configuration
    - Inference parameters
    - System prompts
    - Guardrails
    - Streaming
- Others
    - Compare mode
    - Prompt caching (reduce cost and latency)
- Response
    - Can be exported to JSON
    - Can be viewed as API request
    - Metrics
        - Latency
        - Input token count
        - Output token count
        - Cost

# Optimize model inference for latency
- Use `latency` parameter to make response faster
- Support only limited models and regions

# Submit prompts and generate responses using the API
- Support
    - Invoke model
    - Converse model
    - Streaming
    - Different model type
        - Base model
        - Inference profile
        - Prompt
        - Provisioned throughput
        - Custom model
    - Request body
## Submit a single prompt with InvokeModel
- Check if models support streaming
- Format
    - modelId
    - body
    - accept
    - contentType
    - explicitPromptCaching
    - guardrailIdentifier
    - guardrailVersion
    - trace
- Others
    - inputTokenCount
    - outputTokenCount
    - invocationLatency
    - firstByteLatency
## Carry out a conversation with the Converse API operations
- Support
    - Maintain a conversation multi turns
    - Customize persona and tone
- API
    - Converse
    - ConverseStream
- Converse API supports unified format for many models
### Supported models and model features
- Not support all models and reatures
### Using the Converse API
- Request
    - Model IDs
- Conversation contains
    - Multi rounds
    - Role
    - Content
- Content message
    - Can be customized by configure fields for different modalities (text, image, document, video)
- Inference parameters
    - maxTokens
    - stopSequences
    - temperature
    - topP
- Response
    - Check the API docs

# Use a tool to complete an Amazon Bedrock model response

# Use a computer use tool to complete an Amazon Bedrock model response

# Prompt caching for faster model inference
