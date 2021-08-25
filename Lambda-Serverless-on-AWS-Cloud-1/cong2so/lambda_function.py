import json

def lambda_handler(event, context):
    # TODO implement
    return cong2so(event["a"],event["b"])

def cong2so(a, b):
    return a + b