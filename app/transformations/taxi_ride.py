from pyspark.sql.dataframe import DataFrame

from pyspark.sql.functions import col, year, weekofyear, count, max as spark_max, row_number
from pyspark.sql.window import Window



def transformation(input_df: DataFrame) -> DataFrame:

    # 1. Add Year and Week columns
    df_with_week_and_year = input_df.withColumn("year", year(col("pickup_datetime"))) \
        .withColumn("week", weekofyear(col("pickup_datetime")))

    # 2. Vendor with the most trips per year
    vendor_count_df = df_with_week_and_year.groupBy("vendor_id", "year") \
        .agg(count("*").alias("total_trips"), spark_max("trip_distance").alias("max_distance"))

    # Set a window for sorting vendors, by total trips and distance
    vendor_window_df = Window.partitionBy("year").orderBy(col("total_trips").desc(), col("max_distance").desc(),
                                                       col("vendor_id").asc())

    # Select the vendor with the most trips per year
    top_vendor_df = vendor_count_df.withColumn("rank", row_number().over(vendor_window_df)) \
        .filter(col("rank") == 1)

    # 3. Week with the most trips per year
    week_count_df = df_with_week_and_year.groupBy("year", "week").agg(count("*").alias("week_trips"))
    top_week_df = week_count_df.withColumn("rank", row_number().over(
        Window.partitionBy("year").orderBy(col("week_trips").desc()))) \
        .filter(col("rank") == 1)

    # 4. How many trips did the vendor with the most trips make in the week with the most trips
    vendor_top_week_df = df_with_week_and_year.join(top_vendor_df, ["year", "vendor_id"]) \
        .join(top_week_df, ["year", "week"]) \
        .groupBy("vendor_id", "year", "week") \
        .agg(count("*").alias("vendor_trips_in_top_week"))


    vendor_top_week_df.show()
    # Return DataFrame to be written
    return vendor_top_week_df
