import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from app.transformations.taxi_ride import TaxiRide

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder \
        .master("local[2]") \
        .appName("TaxiRideTest") \
        .getOrCreate()

@pytest.fixture
def sample_data(spark):
    data = [
        ("2021-01-01 10:00:00", 1, 5.0),
        ("2021-01-02 11:00:00", 1, 3.0),
        ("2021-01-03 12:00:00", 2, 7.0),
        ("2021-01-04 13:00:00", 2, 2.0),
        ("2021-01-05 14:00:00", 1, 8.0),
        ("2021-01-06 15:00:00", 2, 1.0),
    ]
    columns = ["pickup_datetime", "vendor_id", "trip_distance"]
    return spark.createDataFrame(data, columns)

def test_add_year_and_week(spark, sample_data):
    taxi_ride = TaxiRide()
    result_df = taxi_ride.add_year_and_week(sample_data)
    result = result_df.collect()

    assert result[0]["year"] == 2021
    assert result[0]["week"] == 53  # Week 53 of 2020 spills into 2021

def test_vendor_with_most_trips_per_year(spark, sample_data):
    taxi_ride = TaxiRide()
    df_with_year_week = taxi_ride.add_year_and_week(sample_data)
    result_df = taxi_ride.vendor_with_most_trips_per_year(df_with_year_week)
    result = result_df.collect()

    assert len(result) == 1
    assert result[0]["vendor_id"] == 1
    assert result[0]["total_trips"] == 3

def test_week_with_most_trips_per_year(spark, sample_data):
    taxi_ride = TaxiRide()
    df_with_year_week = taxi_ride.add_year_and_week(sample_data)
    result_df = taxi_ride.week_with_most_trips_per_year(df_with_year_week)
    result = result_df.collect()

    assert len(result) == 1
    assert result[0]["week"] == 53  # Week 53 of 2020 spills into 2021
    assert result[0]["week_trips"] == 3

def test_vendor_trips_in_top_week(spark, sample_data):
    taxi_ride = TaxiRide()
    df_with_year_week = taxi_ride.add_year_and_week(sample_data)
    top_vendor_df = taxi_ride.vendor_with_most_trips_per_year(df_with_year_week)
    top_week_df = taxi_ride.week_with_most_trips_per_year(df_with_year_week)
    result_df = taxi_ride.vendor_trips_in_top_week(df_with_year_week, top_vendor_df, top_week_df)
    result = result_df.collect()

    assert len(result) == 1
    assert result[0]["vendor_id"] == 1
    assert result[0]["vendor_trips_in_top_week"] == 2

def test_transform(spark, sample_data):
    taxi_ride = TaxiRide()
    result_df = taxi_ride.transform(sample_data)
    result = result_df.collect()

    assert len(result) == 1
    assert result[0]["vendor_id"] == 1
    assert result[0]["vendor_trips_in_top_week"] == 2

