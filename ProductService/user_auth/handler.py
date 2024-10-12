import json
from common.logger import get_logger
from user_auth.service import UserService
from common.exceptions import InvalidCredentialsException

logger = get_logger()

def handler(event, context):
    logger.info("User Authentication Lambda initialized")
    user_service = UserService()
    
    try:
        body = json.loads(event.get('body', '{}'))
        username = body['username']
        password = body['password']
        
        # Autenticar usuario
        token = user_service.authenticate_user(username, password)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User authenticated successfully',
                'token': token
            })
        }
        
    except InvalidCredentialsException as e:
        logger.error(f"Invalid credentials: {str(e)}")
        return {
            'statusCode': 401,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
