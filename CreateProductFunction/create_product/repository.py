import boto3
from botocore.exceptions import ClientError
from common.exceptions import DatabaseError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProductsTable')

def save_product(product):
    try:
        table.put_item(Item=product)
    except ClientError as e:
        raise DatabaseError(f"Failed to save product: {str(e)}")
