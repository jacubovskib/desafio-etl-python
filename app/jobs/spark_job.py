from pyspark.sql import SparkSession
from app.readers.reader import Reader
from app.writers.writer import Writer


class SparkJob:
    def __init__(self):
        self.spark = None
        self.transformation = None
        self.writer = None
        self.reader = None
        self.log = None
        self.output_path = None
        self.input_path = None
        self.app_name = None

    def configure(self, app_name: str, input_path: str, output_path: str, logging, transformation):
        self.app_name = app_name
        self.input_path = input_path
        self.output_path = output_path
        self.log = logging
        self.reader = Reader()
        self.writer = Writer()
        self.transformation = transformation

        # Initializes the Spark session
        self.spark = SparkSession.builder.appName(self.app_name).getOrCreate()
        self.log.info(f"Spark session created: {self.spark.sparkContext.appName}")

        # Initializes the Reader and WWriter Classes
        self.reader.config(self.spark, self.input_path)
        self.writer.config(self.spark, self.output_path)
        
        return self

    def run(self):
         # Read Json files
        input_df = self.reader.json()

        # Execute transformations
        to_write_df = self.transformation(input_df)

        # Writing to csv file
        self.writer.csv(to_write_df)

        self.stop()

    def stop(self):
        self.spark.stop()