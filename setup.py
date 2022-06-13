from setuptools import find_packages, setup
from pyspark_logging_examples import __version__

setup(
    name="pyspark_logging_examples",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author="",
)
