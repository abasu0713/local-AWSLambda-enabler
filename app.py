import json 
import logging


logger = logging.getLogger()

def handler(event, context): 
    print("Event: " + json.dumps(event, indent=2))
    logger.debug("event recieved by Lambda: {}".format(json.dumps(event, indent=1)))
    return {
        'statusCode': 200,
        'body': "Base python container for Lambda completed successfully!"
    }
