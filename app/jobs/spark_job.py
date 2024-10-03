from pyspark.sql import SparkSession
from readers.reader import Reader
from writers.writer import Writer
from transformations.taxi_ride import TaxiRide

class SparkJob:
    def __init__(self):
        self.spark: SparkSession = None
        self.transformation: TaxiRide = None
        self.writer: Writer = None
        self.reader: Reader = None
        self.log = None
        self.output_path: str = None
        self.input_path: str = None
        self.app_name: str = None

    def configure(self, app_name: str, input_path: str, output_path: str, logging, TransformationClass: TaxiRide):
        self.app_name = app_name
        self.input_path = input_path
        self.output_path = output_path
        self.log = logging
        self.reader = Reader()
        self.writer = Writer()
        self.transformation = TransformationClass()

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
        to_write_df = self.transformation.transform(input_df)

        # Writing to csv file
        self.writer.csv(to_write_df)

        self.stop()

    def stop(self):
        self.spark.stop()