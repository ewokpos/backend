import json
from common.logger import get_logger
from create_product.service import SaleService
from common.exceptions import BadRequestException

logger = get_logger()

def handler(event, context):
    logger.info("Create Sale Lambda initialized")
    sale_service = SaleService()
    
    try:
        body = json.loads(event.get('body', '{}'))
        
        # Crear la venta usando el servicio
        sale = sale_service.create_sale(body)
        
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Sale registered successfully',
                'sale': sale
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
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
