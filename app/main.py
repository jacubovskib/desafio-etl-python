import logging
import sys

from pyspark.sql import SparkSession
from app.jobs.spark_job import SparkJob
from app.transformations.taxi_ride import transformation

LOG_FILENAME = "taxti-riders"


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    args = sys.argv

    logging.info(f"Arguments: {args}, lenth: {len(args)}")
    logging.info("Starting the application")

    input_path = args[1]
    output_path = args[2]
    app_name = args[3]

    
    spark = SparkSession.builder.appName("myapp").getOrCreate()

    SparkJob()\
        .configure(
            app_name=app_name,
            input_path=input_path,
            output_path=output_path,
            logging=logging,
            transformation=transformation)\
        .run()

    logging.info("Stopping the application")
    sys.exit(0)