from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import col, count, max as spark_max, row_number, year, weekofyear


class TaxiRide:
    def add_year_and_week(self, df: DataFrame) -> DataFrame:
        return df.withColumn("year", year(col("pickup_datetime"))) \
                 .withColumn("week", weekofyear(col("pickup_datetime")))

    def vendor_with_most_trips_per_year(self, df: DataFrame) -> DataFrame:
        vendor_count_df = df.groupBy("vendor_id", "year") \
            .agg(count("*").alias("total_trips"), spark_max("trip_distance").alias("max_distance"))

        vendor_window = Window.partitionBy("year").orderBy(col("total_trips").desc(), col("max_distance").desc(),
                                                           col("vendor_id").asc())

        return vendor_count_df.withColumn("rank", row_number().over(vendor_window)) \
                              .filter(col("rank") == 1)

    def week_with_most_trips_per_year(self, df: DataFrame) -> DataFrame:
        week_count_df = df.groupBy("year", "week").agg(count("*").alias("week_trips"))

        week_window = Window.partitionBy("year").orderBy(col("week_trips").desc())

        return week_count_df.withColumn("rank", row_number().over(week_window)) \
                            .filter(col("rank") == 1)

    def vendor_trips_in_top_week(self, df_with_week_and_year: DataFrame, top_vendor_df: DataFrame, top_week_df: DataFrame) -> DataFrame:
        return df_with_week_and_year.join(top_vendor_df, ["year", "vendor_id"]) \
                                    .join(top_week_df, ["year", "week"]) \
                                    .groupBy("vendor_id", "year", "week") \
                                    .agg(count("*").alias("vendor_trips_in_top_week"))

    def transform(self, input_df: DataFrame) -> DataFrame:
        # Pass input_df through the sequence of transformations
        df_with_week_and_year = self.add_year_and_week(input_df)
        top_vendor_df = self.vendor_with_most_trips_per_year(df_with_week_and_year)
        top_week_df = self.week_with_most_trips_per_year(df_with_week_and_year)
        result_df = self.vendor_trips_in_top_week(df_with_week_and_year, top_vendor_df, top_week_df)
        
        return result_df