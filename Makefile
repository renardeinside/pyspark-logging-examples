ifneq (,$(wildcard ./.env))
    include .env
    export
endif

export SPARK_CONF_DIR=$(PWD)/conf/local

run-tests:
	pytest tests

run-python:
	pyspark

upload-log-configuration:
	databricks --profile=$(DATABRICKS_CLI_PROFILE) fs mkdirs dbfs:/logs-config
	databricks --profile=$(DATABRICKS_CLI_PROFILE) fs cp -r --overwrite conf/databricks dbfs:/logs-config