import logging
import sys

from pyspark.sql import SparkSession
from jobs.spark_job import SparkJob
from transformations.taxi_ride import TaxiRide

LOG_FILENAME = "taxti-riders"


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    args = sys.argv

    logging.info(f"Arguments: {args}, lenth: {len(args)}")
    logging.info("Starting the application")

    input_path = args[1]
    output_path = args[2]
    app_name = args[3]

    logging.info(f"Input path: {input_path}")
    logging.info(f"Output path: {output_path}")
    logging.info(f"App name: {app_name}")
    
    spark = SparkSession.builder.appName("myapp").getOrCreate()

    SparkJob()\
        .configure(
            app_name=app_name,
            input_path=input_path,
            output_path=output_path,
            logging=logging,
            TransformationClass=TaxiRide)\
        .run()

    logging.info("Stopping the application")
    sys.exit(0)