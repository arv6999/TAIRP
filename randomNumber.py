import json
import random

def lambda_handler(event, context):
    random_number = random.randint(1, 100)
    response = {
        "statusCode": 200,
        "body": json.dumps({"random_number": random_number})
    }
    return response
