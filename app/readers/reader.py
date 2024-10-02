from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession


class Reader:
    def __init__(self, spark: SparkSession = None, input_path: str = None):
        self.spark = spark
        self.input_path = input_path

    def config(self, spark: SparkSession, input_path: str = None):
        self.spark = spark
        self.input_path = input_path


    def json(self) -> DataFrame:
        return self.spark.read.json(self.input_path)
