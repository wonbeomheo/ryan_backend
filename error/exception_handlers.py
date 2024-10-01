from rest_framework.views import exception_handler
import logging

logger = logging.getLogger('dev.error')

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    logger.error(exc)    
    if response is not None:
        response.data['status_code'] = response.status_code
        
    return response