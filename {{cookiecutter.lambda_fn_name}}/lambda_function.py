#!/usr/bin/env python
import json
import os


def lambda_handler(event, context):
    '''The Lambda function handler
    '''
    if 'LAMBDA_CONFIG' in os.environ:
        config = json.loads(os.getenv('LAMBDA_CONFIG'))
    else:
        with open('config.json') as f:
            config = json.load(f)

    # Get normal key
    value = config['key']
    return value
