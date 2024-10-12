import json
from common.logger import get_logger
from update_product.service import ProductService  # Apunta al service de update_product
from common.exceptions import BadRequestException, ProductNotFoundException

logger = get_logger()

def handler(event, context):
    logger.info("Update Product Lambda initialized")
    product_service = ProductService()
    
    try:
        # Obtener ID del producto desde los parámetros de ruta
        product_id = event['pathParameters']['id']
        body = json.loads(event.get('body', '{}'))
        
        # Actualizar producto
        updated_product = product_service.update_product(product_id, body)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Product updated successfully',
                'product': updated_product
            })
        }
    except BadRequestException as e:
        logger.error(f"Bad request: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
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
