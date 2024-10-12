import json
from common.logger import get_logger
from delete_product.service import ProductService  # Apunta al service de delete_product
from common.exceptions import ProductNotFoundException

logger = get_logger()

def handler(event, context):
    logger.info("Delete Product Lambda initialized")
    product_service = ProductService()
    
    try:
        # Obtener el ID del producto desde los parámetros de ruta
        product_id = event['pathParameters']['id']
        
        # Eliminar producto usando el servicio
        product_service.delete_product(product_id)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Product deleted successfully'})
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