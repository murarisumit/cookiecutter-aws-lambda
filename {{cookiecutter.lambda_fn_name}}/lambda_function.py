#!/usr/bin/env python
'''
Parse an SNS event message and send to a Slack Channel
'''
import boto3
from base64 import b64decode
import json
import os
import requests


def lambda_handler(event, context):
    '''The Lambda function handler
    '''
    if 'LAMBDA_CONFIG' in os.environ:
        config = json.loads(os.getenv('LAMBDA_CONFIG'))
    else:
        with open('config.json') as f:
            config = json.load(f)

    # Keep encryped variables in kms.
    WEBHOOK_URL = "https://" + boto3.client('kms').decrypt(
        CiphertextBlob=b64decode(config['encrypted_token']))['Plaintext'].decode('utf-8')

    # Get normal key
    value = config['key']

    payload = {'text': value}
    print('DEBUG:', payload)
    r = requests.post(WEBHOOK_URL, json=payload)
    return r.status_code
