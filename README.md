# PySpark logging examples in local environment and on Databricks clusters

This repo contains examples on how to configure PySpark logs in the local Apache Spark environment and when using Databricks clusters.

[Link to the blogpost with details](https://polarpersonal.medium.com/writing-pyspark-logs-in-apache-spark-and-databricks-8590c28d1d51).

## Local setup

Provide your logging configurations in `conf/local/log4j.properties` and pass this path via `SPARK_CONF_DIR` when initializing the Python session.

## Databricks setup

* Describe your logging configurations in `conf/databricks/driver-log4j.properties`. 
* Provide your `DATABRICKS_CLI_PROFILE` environment variable in the `.env` file
* Upload the configurations to DBFS via `make upload-log-configuration`
* Add the init script in the cluster properties

