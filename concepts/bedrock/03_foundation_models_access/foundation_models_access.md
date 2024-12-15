# Access Amazon Bedrock foundation models
- Access is not granted by default
- Have to request access via console
- IAM role is required to manage access to FMs
# Grant IAM permissions to request access to Amazon Bedrock foundation models
- Attach identity-based IAM policy with these actions
    - aws-marketplace:Subscribe
    - aws-marketplace:Unsubscribe
    - aws-marketplace:ViewSubscriptions
## Control access by configure model product ID
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow|Deny",
            "Action": [
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws-marketplace:ProductId": [
                        model-product-id-1,
                        model-product-id-2,
                        ...
                    ]
                }
            }
        },
        {
            "Effect": "Allow|Deny",
            "Action": [
                "aws-marketplace:Unsubscribe"
                "aws-marketplace:ViewSubscriptions"
            ],
            "Resource": "*"
        }
    ]
}
```
# Add or remove access to Amazon Bedrock foundation models
- Can not remove request access from AWS Titan, Mistral and Llama3. Have to use IAM policy to deny access
- Support these actions in console