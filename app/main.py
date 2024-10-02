import logging
import sys

from pyspark.sql import SparkSession


LOG_FILENAME = ""


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    args = sys.argv

    logging.info(f"Arguments: {args}, lenth: {len(args)}")
    logging.info("Starting the application")

    input_path = args[1]
    output_path = args[2]
    app_name = args[3]

    
    spark = SparkSession.builder.appName("myapp").getOrCreate()
    spark.stop()
    logging.info("Stopping the application")
    sys.exit(0)