import json
from common.logger import get_logger
from get_product.service import ProductService
from common.exceptions import ProductNotFoundException

logger = get_logger()

def handler(event, context):
    logger.info("Get Product Lambda initialized")
    product_service = ProductService()
    
    try:
        # Obtener el ID del producto desde los parámetros de ruta
        product_id = event['pathParameters']['id']
        
        # Obtener producto desde el servicio
        product = product_service.get_product(product_id)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Product retrieved successfully',
                'product': product
            })
        }
    except ProductNotFoundException as e:
        logger.error(f"Product not found: {str(e)}")
        return {
            'statusCode': 404,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
