import json
import traceback
from common.logger import get_logger
from create_product.service import ProductService
from common.exceptions import BadRequestException

# Inicializar logger
logger = get_logger()

def handler(event, context):
    logger.info("Lambda handler initialized")
    product_service = ProductService()
    try:
        body = json.loads(event.get('body', '{}'))
        product = product_service.create_product(body)
        
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
        logger.error(f"Unhandled error: {str(e)}")
        logger.error(f"Stack trace: {traceback.format_exc()}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
