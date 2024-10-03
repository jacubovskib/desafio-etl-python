### ETL Spark 
Repositório do desafio ETL Spark

#### Run the job

```bash
poetry build && poetry run spark-submit \
    --master local \
    --py-files "dist/etl-spark-*.whl" \
    app/main.py \
    /home/nobre/workspace/etl-spark/resources/input-data/*.json \
    /home/nobre/workspace/etl-spark/output \
    "ETL PySpark Desafio"
```

