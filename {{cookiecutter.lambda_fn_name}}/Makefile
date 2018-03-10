VIRTUAL_ENV = $(PWD)/venv

export

develop:
	virtualenv -p `which python3` ${VIRTUAL_ENV}
	${VIRTUAL_ENV}/bin/pip install -r requirements.txt

test:
	python lambda_test.py

create:
	./virtualenv-lambda-push.sh create

update:
	./virtualenv-lambda-push.sh update

clean:
	rm -rf {{cookiecutter.lambda_fn_name}}.zip

get-fn-arn:
	aws lambda get-function --function-name function:{{cookiecutter.lambda_fn_name}} --query Configuration.FunctionArn --output text
