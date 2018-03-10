import json
from lambda_function import lambda_handler

json_input = json.loads(r"""
{
  "Records": [
    {
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
      "EventSource": "aws:sns",
      }
  ]
}""")
print('running locally')
print(lambda_handler(json_input, None))
