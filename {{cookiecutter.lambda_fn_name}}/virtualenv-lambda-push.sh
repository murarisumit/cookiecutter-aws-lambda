#!/bin/bash
#
# Recommended environment variables:
#   AWS_REGION
#   AWS_PROFILE
#
set -x
zip -u {{cookiecutter.lambda_fn_name}}.zip lambda_function.py config.json
pushd $VIRTUAL_ENV/lib/python3.6/site-packages
zip -u -r $OLDPWD/{{cookiecutter.lambda_fn_name}}.zip . \
  --exclude pip\* \
  --exclude setuptools\* \
  --exclude virtualenv\*
popd

case $1 in
  ( create )
    aws lambda create-function \
     --function-name {{cookiecutter.lambda_fn_name}} \
     --runtime python3.6 \
     --role arn:aws:iam::{{cookiecutter.account_id}}:role/lambda_basic_execution \
     --handler lambda_function.lambda_handler \
     --zip-file fileb://./{{cookiecutter.lambda_fn_name}}.zip \
     --description "{{cookiecutter.description}}" \
     --memory-size 128 \
     --timeout 3
    ;;
  ( update )
    aws lambda update-function-code \
      --function-name function:{{cookiecutter.lambda_fn_name}} \
      --zip-file fileb://./{{cookiecutter.lambda_fn_name}}.zip
    ;;
  ( * )
    echo "USAGE: $0 [create|update]" 1>&2
    exit 255
    ;;
esac
