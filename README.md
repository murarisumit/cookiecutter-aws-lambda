First, get Cookiecutter. Trust me, it's awesome:

`$ pip install "cookiecutter>=1.4.0"`

Now run it against this repo:

`$ cookiecutter https://github.com/murarisumit/cookiecutter-aws-lambda`

You'll be prompted for some values. Provide them, and you'll have aws lambda function file structure created.


* Create Lambda IAM Role for execution : 
    * The Lambda function requires an IAM Role to execute.
    * You can create this in the AWS IAM console or the AWS CLI.
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

* Create IAM Role Policy : To permit the IAM Role above to execute and put logs in CloudWatch Logs:
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

* Create a virtualenv and install packages: 
    ```shell
    make develop
    ```

* Activate virtualenv`source venv/bin/activate`

* Run it locally
    ```shell
    make test
    ```

* Creating lambda function 
    ```shell
    make create
    ```

* Update lambda function 
    ```shell
    make update
    ```

* View and get lambda [arn](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
    ```shell
    make get-fn-arn
    ```

