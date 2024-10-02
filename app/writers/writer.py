from pyspark.sql import DataFrame
from pyspark.sql.connect.session import SparkSession


class Writer:
    def __init__(self, spark: SparkSession = None, output_path: str = None):
        self.spark = spark
        self.output_path = output_path

    def config(self, spark: SparkSession, output_path: str = None):
        self.spark = spark
        self.output_path = output_path

    def csv(self, data_frame: DataFrame, mode: str = "overwrite", header: bool = True, coalesce=1):
        data_frame.coalesce(coalesce).write.mode(mode).csv(self.output_path, header=header)

