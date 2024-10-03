# ETL com PySpark

Este projeto é uma solução de ETL (Extract, Transform, Load) utilizando PySpark. O objetivo é processar dados de viagens de táxi em Nova York, realizando agregações e transformações para extrair insights, como identificar o fornecedor com o maior número de viagens e a semana com o maior número de viagens.

## Estrutura de Pastas

A estrutura de diretórios do projeto é organizada da seguinte forma:

```

etl-spark/
├── app/
│   ├── __init__.py
│   ├── jobs/
|   ├───── spark_job.py          # Script principal que executa o processo de ETL
│   ├── readers/
|   ├───── reader.py             # Classe que implementa um leitor de arquivos json
│   ├── tests/
|   ├───── integration/
├   ├────────── test_taxi_ride_integration.py            # Teste de integração 
├   ├────────── test_validate_spark_environment.py       # Teste de integração para o environment.
|   ├───── unit/                                         
├   ├────────── test_taxi_ride.py                        # Teste de unidade para classe de transformação
│   ├── transformations/
|   ├───── taxi_ride.py          # Contém a classe com as transformações de dados
│   ├── writers/
|   ├───── writer.py   
├── resources/
│   ├── input-data/             # Dados de entrada em formato JSON
├── output/                     # Pasta que armazena o resultado
├── dist/                       # Pacote distribuível (construído com poetry)
├── .gitignore                  # Especifica quais arquivos e/ou diretorios a serem ignorados
├── pyproject.toml              # Dependências do projeto gerenciadas pelo Poetry
├── .gitpod.Dockerfile          # arquivo usado no ambiente de desenvolvimento Gitpod para personalizar a imagem Docker
├── .gitpod.yaml                # O arquivo para configurar o ambiente de desenvolvimento no Gitpod
├── .pylintrc                   # Arquivo de configuração do Lint
├── README.md                   # Documentação do projeto

└── requirements.txt            # Dependências do projeto

```

## Dependências

Este projeto utiliza as seguintes bibliotecas e ferramentas:

- **Python 3.11+**
- **Apache Spark 3.5.1**
- **PySpark  3.5.1**
- **Poetry** (para gerenciamento de dependências)
- **pytest** (para testes unitários)
- **Java 11+** (para testes unitários)
  
Instale as dependências com Poetry:

```bash
poetry install
```

## Como Executar o Projeto

### 1. Executando com Spark-Submit

Para rodar o processo ETL via `spark-submit`, você pode utilizar o seguinte comando:

```bash
poetry build && poetry run spark-submit \
    --master local \
    --py-files "dist/etl_spark-*.whl" \
    app/main.py \
    /caminho/para/input-data/*.json \
    /caminho/para/output-data \
    "Nome da Aplicação"
```

Esse comando:
- Compila o pacote PySpark (`etl_spark-*.whl`) usando o Poetry.
- Usa o `spark-submit` para rodar o script `main.py`, que executa o pipeline de ETL.
- Processa os arquivos de entrada na pasta especificada (`input-data`) e escreve os resultados na pasta de saída (`output-data`).

### 2. Executando Testes

Os testes de unidade e integração foram implementados utilizando o framework `pytest`. Para executar os testes, utilize o seguinte comando:

```bash
poetry run pytest app/tests/integration  

poetry run pytest app/tests/unit  
```

Os testes verificam as principais transformações e agregações do projeto para garantir que os resultados estejam corretos.

## Estrutura de Transformações

As transformações de dados estão encapsuladas na classe `TaxiRide`, localizada em `app/transformations/taxi_ride.py`. A classe contém métodos responsáveis por adicionar colunas de ano e semana, calcular o fornecedor com mais viagens por ano, identificar a semana com mais viagens e calcular quantas viagens o fornecedor principal fez na semana principal.

O pipeline de transformação completo é executado através do método `transform()`.
