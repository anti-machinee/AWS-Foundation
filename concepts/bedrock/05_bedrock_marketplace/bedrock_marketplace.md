# Amazon Bedrock Marketplace
- Discover models are not supported officially by Bedrock
- Guide
    - Discover models in a single catalog
    - Subscribe it
    - Deploy to an endpoint managed by SageMaker AI
    - Access these models via API
- Access via
    - Operation (not all)
    - Console

# Set up Amazon Bedrock Marketplace
- Prepare
    - Managed policy to use Bedrock API
    - Policy to use Bedrock Management Console
- To encrypt the endpoint, prepare KMS policy

# End to end workflow
- Can use SDK to include
    - List models
    - Describe model
    - Create endpoint
    - Describe endpoint
    - Wait for endpoint created
    - Invoke endpoint
    - Converse endpoint
    - List endpoints
    - Update enpoint
    - Deregister endpoint
    - Register endpoint
    - Delete endpoint

# Discover a model
- Use console

# Subscribe to a model
- Pay cost to use model
- Cost is separated from Sagemaker AI infrastructure cost

# Deploy a model
- Select
    - Name endpoint
    - Select number of instances
    - Choose instance type
    - VPC
    - Access role
    - Encryption
    - Tags
- SageMaker service role automatically created to assume and perform actions
- If endpoints are fail due to modifications, deregister and register endpoints.

# Bring your own endpoint
- TODO: not clear

# Call the endpoint
- Can be called after deployed
- Call type including converse and invoke

# Manage your endpoints
- Actions
    - Change number of instances, instance types
    - Change tags
    - Delete endpoints
- Support
    - Console
    - API

# Model compatibility
- Support
    - Invoke for all models
    - Converse for not all models
