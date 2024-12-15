import boto3


def print_caller_identity():
    sts_client = boto3.client('sts')
    response = sts_client.get_caller_identity()
    
    print("Caller Identity Details:")
    print(f"  ARN: {response['Arn']}")
    print(f"  Account: {response['Account']}")
    print(f"  User ID: {response['UserId']}")


if __name__ == "__main__":
    print_caller_identity()
