from pyspark_logging_examples.common import Workload
from sklearn.datasets import fetch_california_housing
import pandas as pd


class SampleLoggingJob(Workload):
    def launch(self):
        self.logger.debug("some debugging message")
        self.logger.info("some info message")
        self.logger.warn("some warning message")
        self.logger.error("some error message")
        self.logger.fatal("some fatal message")

        _cnt = self.spark.range(1000).count()


def entrypoint():  # pragma: no cover
    job = SampleLoggingJob()
    job.launch()


# if you're using spark_python_task, you'll need the __main__ block to start the code execution
if __name__ == "__main__":
    entrypoint()
