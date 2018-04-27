import json
from lambda_function import lambda_handler
data = """
{
  "Records": [
    {
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
      "EventSource": "aws:sns"
    }
  ]

}"""
json_input = json.loads(data)
print("running locally")
print(lambda_handler(json_input, None))
