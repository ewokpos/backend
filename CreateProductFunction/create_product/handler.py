import json
from create_product.service import create_product_service
from common.logger import get_logger
from common.exceptions import BadRequestException

logger = get_logger()

def handler(event, context):
    try:
        logger.info(f"Event: {event}")
        body = json.loads(event.get('body', '{}'))
        
        # Llamar al servicio de creación de producto
        product = create_product_service(body)

        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Product created successfully',
                'product': product
            })
        }
    except BadRequestException as e:
        logger.error(f"Bad request: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
