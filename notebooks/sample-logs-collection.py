# Databricks notebook source
from pyspark.sql import SparkSession
from typing import Optional

NOTEBOOK_PATH = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .notebookPath()
    .get()
)
FORMATTED_NOTEBOOK_PATH = (
    NOTEBOOK_PATH.lower().replace("/", ".") + "."
)  # add trailing dot


class LoggerProvider:
    def get_logger(self, spark: SparkSession, custom_prefix: Optional[str] = ""):
        log4j_logger = spark._jvm.org.apache.log4j  # noqa
        return log4j_logger.LogManager.getLogger(custom_prefix + self.__full_name__())

    def __full_name__(self):
        klass = self.__class__
        module = klass.__module__
        if module == "__builtin__":
            return klass.__name__  # avoid outputs like '__builtin__.str'
        return module + "." + klass.__name__


# COMMAND ----------

logger = LoggerProvider().get_logger(
    spark, custom_prefix="notebooks" + FORMATTED_NOTEBOOK_PATH
)

# COMMAND ----------

logger.info("some info message")
logger.warn("some warning message")
logger.fatal("some fatal message")

# COMMAND ----------
