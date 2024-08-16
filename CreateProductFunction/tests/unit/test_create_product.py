import pytest
import boto3
from unittest.mock import patch, MagicMock
from create_product.handler import handler
from decimal import Decimal
import json

@pytest.fixture
def dynamodb_setup():
    with patch('boto3.resource') as mock_dynamodb_resource:
        mock_table = MagicMock()
        mock_dynamodb_resource.return_value.Table.return_value = mock_table
        yield mock_table

def test_create_product_success(dynamodb_setup):
    event = {
        "body": '{"name": "Product 1", "category": "Category 1", "price": 10.99, "stock": 5}'
    }
    dynamodb_setup.put_item.return_value = {}
    response = handler(event, None)
    assert response['statusCode'] == 201
    assert 'Product created successfully' in response['body']

def test_create_product_missing_name(dynamodb_setup):
    event = {
        "body": '{"category": "Category 1", "price": 10.99, "stock": 5}'
    }
    response = handler(event, None)
    assert response['statusCode'] == 400

def test_create_product_invalid_price(dynamodb_setup):
    event = {
        "body": '{"name": "Product 1", "category": "Category 1", "price": -10.99}'
    }
    response = handler(event, None)
    assert response['statusCode'] == 400