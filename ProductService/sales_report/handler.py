import json
from common.logger import get_logger
from reports.service import ReportService

logger = get_logger()

def handler(event, context):
    logger.info("Sales Report Lambda initialized")
    report_service = ReportService()
    
    try:
        query_params = event.get('queryStringParameters', {})
        
        report = report_service.get_sales_report(query_params)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Sales report generated successfully',
                'report': report
            })
        }
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
