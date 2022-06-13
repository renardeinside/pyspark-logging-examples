from pyspark_logging_examples.workloads.sample_logging_job import SampleLoggingJob
from pyspark.sql import SparkSession
from pathlib import Path
import logging


def test_sample_logging_job(spark: SparkSession):
    logging.info("Testing the sample logging job")
    etl_job = SampleLoggingJob(spark, {})
    etl_job.launch()
    logging.info("Testing the sample logging job - done")
