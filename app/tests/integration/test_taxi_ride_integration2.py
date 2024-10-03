import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from app.transformations.taxi_ride import TaxiRide

class TaxiRideIntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("TaxiRideIntegrationTest") \
            .master("local[*]") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_transform(self):
        # Dados de exemplo
        data = [
            (1, "2023-01-01 10:00:00", 5.0),
            (1, "2023-01-02 11:00:00", 3.0),
            (2, "2023-01-01 12:00:00", 7.0),
            (2, "2023-01-08 13:00:00", 2.0),
            (1, "2023-01-08 14:00:00", 6.0)
        ]
        columns = ["vendor_id", "pickup_datetime", "trip_distance"]
        input_df = self.spark.createDataFrame(data, columns)

        # Instanciar a classe TaxiRide
        taxi_ride = TaxiRide()

        # Chamar o método transform
        result_df = taxi_ride.transform(input_df)

        # Verificar a saída
        expected_data = [
            (1, 2023, 1, 2)
        ]
        expected_columns = ["vendor_id", "year", "week", "vendor_trips_in_top_week"]
        expected_df = self.spark.createDataFrame(expected_data, expected_columns)

        # Ordenar os DataFrames para comparação
        result_df_sorted = result_df.orderBy(col("vendor_id"), col("year"), col("week"))
        expected_df_sorted = expected_df.orderBy(col("vendor_id"), col("year"), col("week"))
        expected_df_sorted.show()
        result_df_sorted.show() 
        # Comparar os DataFrames
        self.assertTrue(result_df_sorted.collect() == expected_df_sorted.collect())

if __name__ == "__main__":
    unittest.main()