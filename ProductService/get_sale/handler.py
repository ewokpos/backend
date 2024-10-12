import json
from common.logger import get_logger
from sales.service import SaleService
from common.exceptions import SaleNotFoundException

logger = get_logger()

def handler(event, context):
    logger.info("Get Sale Lambda initialized")
    sale_service = SaleService()
    
    try:
        # Obtener ID de la venta
        sale_id = event['pathParameters']['id']
        
        # Obtener la venta
        sale = sale_service.get_sale(sale_id)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Sale retrieved successfully',
                'sale': sale
            })
        }
    except SaleNotFoundException as e:
        logger.error(f"Sale not found: {str(e)}")
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
