# {{cookiecutter.lambda_fn_name}} AWS Lambda Function

**Reference to project structure is taken from `https://github.com/robbwagoner/aws-lambda-sns-to-slack`**

### This project's configuration file
`config.json`


## Development and testing locally

* Create a virtualenv and install packages: 
    ```shell
    make develop
    ```
* `source venv/bin/activate`

* Run it locally
    ```shell
    make test
    ```

#### Lambda IAM Role for execution

The Lambda function requires an IAM Role to execute.
You can create this in the AWS IAM console or the AWS CLI.

```shell
$ aws iam create-role --role-name lambda_basic_execution --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

#### IAM Role Policy

To permit the IAM Role above to execute and put logs in CloudWatch Logs:

```shell
aws iam put-role-policy --role-name lambda_basic_execution --policy-name lambda_basic_execution --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}'
```


The Role name `lambda_basic_execution` is created by the AWS Lambda console.

The ARN: *arn:aws:iam::<AWS_ACCOUNT_ID>:role/lambda_basic_execution*


#### Creating lambda function 
```shell
make create
```

#### Update lambda function 
```shell
make update
```

#### Get lambda [arn](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
```shell
make get-fn-arn
```


### Create version aliases for development, test, staging, production, etc

```shell
aws lambda create-alias \
  --function-name {{cookiecutter.lambda_fn_name}} \
  --description "development version" \
  --function-version "\$LATEST" \
  --name development
```

```shell
aws lambda publish-version \
  --function-name {{cookiecutter.lambda_fn_name}}
```



### Lambda Resources
* https://docs.aws.amazon.com/lambda/latest/dg/python-lambda.html
* https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
* https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html

