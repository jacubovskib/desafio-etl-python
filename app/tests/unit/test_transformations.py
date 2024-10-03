# test_transformation.py

import pytest
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

from app.transformations.taxi_ride import transformation

@pytest.fixture(scope="module")
def spark():
    """Cria uma sessão Spark para os testes."""
    spark = SparkSession.builder \
        .master("local") \
        .appName("Test Transformation") \
        .getOrCreate()
    yield spark
    spark.stop()


def test_transformation(spark):
    data = [
        Row(vendor_id="V1", pickup_datetime="2023-01-01 10:00:00", trip_distance=10.0),
        Row(vendor_id="V1", pickup_datetime="2023-01-02 11:00:00", trip_distance=5.0),
        Row(vendor_id="V2", pickup_datetime="2023-01-01 12:00:00", trip_distance=7.0),
        Row(vendor_id="V2", pickup_datetime="2023-01-02 13:00:00", trip_distance=15.0)
    ]

    input_df = spark.createDataFrame(data)

    # Chamar a função que está sendo testada
    result_df = transformation(input_df)

    # Esperado: V1 deve ter 2 viagens e 10.0 como a maior distância, V2 deve ter 2 viagens e 15.0 como a maior distância
    expected_data = [
        Row(vendor_id="V2", year=2023, week=52, vendor_trips_in_top_week=1)
    ]

    expected_df = spark.createDataFrame(expected_data)


    # Verificar se os resultados são iguais
    assert result_df.collect() == expected_df.collect()
