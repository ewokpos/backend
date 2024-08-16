from common.exceptions import BadRequestException

def validate_product_data(data):
    if 'name' not in data or not data['name']:
        raise BadRequestException("Product name is required")
    if 'category' not in data or not data['category']:
        raise BadRequestException("Product category is required")
    if 'price' not in data or not isinstance(data['price'], (int, float)) or data['price'] < 0:
        raise BadRequestException("Product price must be a positive number")
