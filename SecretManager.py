import json
import boto3
from botocore.exceptions import ClientError

def get_secret():

    secret_name = "GeminiAPIKey"
    region_name = "us-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    API_KEY = get_secret_value_response['SecretString']
    
    json_string = '{"GeminiAPIKey":"AIzaSyAA0q_TyBT0GKKx36n32arRl-1kem8-aoQ"}'

    # Parse the JSON
    data = json.loads(json_string)

    # Extract the API key
    api_key = data["GeminiAPIKey"]

    return api_key

def get_database_cred():

    secret_name = "MongoDB"
    region_name = "us-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    
    return secret
