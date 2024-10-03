# import unittest
# from pyspark.sql import SparkSession
# import os
# import logging

# from app.jobs.spark_job import SparkJob
# from app.transformations.taxi_ride import transformation

# class TestIntegrationTaxiRide(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.spark = SparkSession.builder.master("local").appName("test").getOrCreate()

#     @classmethod
#     def tearDownClass(cls):
#         cls.spark.stop()

#     def test_integration_execute(self):
#         input_path = "/home/nobre/workspace/etl-spark/resources/input-data/data-nyctaxi-trips-2009.json"
#         output_path = "/home/nobre/workspace/etl-spark/resources/output-data"

#         # Executar a função principal
#         SparkJob()\
#                 .configure(
#                     app_name="test integration",
#                     input_path=input_path,
#                     output_path=output_path,
#                     logging=logging,
#                     transformation=transformation)\
#                 .run()
        
#         # Verificar se o arquivo de saída foi criado
#         output_files = os.listdir(output_path)
#         self.assertGreater(len(output_files), 0, "Nenhum arquivo foi criado no diretório de saída")

#         # Ler o arquivo de saída e verificar os resultados
#         result_df = self.spark.read.csv(output_path, header=True)
#         self.assertGreater(result_df.count(), 0, "O arquivo de saída está vazio")

#         # Verificar se a lógica foi aplicada corretamente (ajuste conforme necessário)
#         self.assertIn("vendor_id", result_df.columns)
#         self.assertIn("vendor_trips_in_top_week", result_df.columns)


# if __name__ == '__main__':
#     unittest.main()