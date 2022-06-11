"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup
from pyspark_logging_examples import __version__

setup(
    name="pyspark_logging_examples",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    entry_points={
        "console_scripts": [
            "etl = pyspark_logging_examples.workloads.sample_etl_job:entrypoint",
            "ml = pyspark_logging_examples.workloads.sample_ml_job:entrypoint",
        ]
    },
    version=__version__,
    description="",
    author="",
)
