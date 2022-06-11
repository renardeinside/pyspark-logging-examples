export SPARK_CONF_DIR=$(PWD)/conf/local

run-tests:
	pytest tests

run-python:
	python