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
- A tool is a function calling. Give a model access to tools that can help to generate
- You call tool on the model's behalf. The tool implementation is an API. 
- The tool can be database, lambda function or other software
## Call a tool with the Converse API
- Send message and definition for tools to the model
- If model determines one of tools can help generate a response, it returns a request for you to use the tool and send the tool results back to model
- The model uses the results to generate a response to original message

# Use a computer use tool to complete an Amazon Bedrock model response
- TODO: 

# Prompt caching for faster model inference
- Add portions of conversations to a cache. Model can reuse the context
- Can use to cache documents (when users upload) to context
- Cache checkpoint
    - Require to use mimimum number of tokens. If add cache checkpoint but less than minimum, checkpoint is not added to cache
- Time to live (TTL)
    - Reset with each successful cache hit
    - Context in cache is preserved in TTL
    - If no cache hits occur, cache expires
    - Can reuse previous cached context
- Support
    - Need to check
    - Quite limited
- 