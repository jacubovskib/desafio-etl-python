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
└───────── writer.py   
```

## Dependências

Este projeto utiliza as seguintes bibliotecas e ferramentas:

- **Python 3.11+**
- **Apache Spark 3.5.1**
- **PySpark  3.5.1**
- **Poetry** (para gerenciamento de dependências)
- **pytest** (para testes unitários)
- **Java 11+** 

## Makefile


#### `make setup`

Executa o processo de configuração inicial do ambiente. Este comando realiza as seguintes tarefas:

1. Torna o script `setup/setup.sh` executável (`chmod +x`).
2. Executa o script `setup/setup.sh`, que:
   - Verifica e cria os diretórios necessários (`output` e `resources/input-data`).
   - Verifica se o `Poetry` está instalado, e caso não esteja, realiza sua instalação.
3. Após o setup inicial, chama o comando `make install` para instalar as dependências do projeto usando o `Poetry`.

#### `make install`

Instala todas as dependências do projeto especificadas no arquivo `pyproject.toml` utilizando o gerenciador de dependências `Poetry`.

#### `make test`

Executa os testes unitários utilizando o `pytest`. Este comando garante que o ambiente esteja configurado corretamente antes de executar o pipeline ETL ou realizar outros desenvolvimentos no projeto.

#### `make build`

Constrói o pacote distribuível do projeto utilizando o `Poetry`. Isso cria um pacote `.whl` e um arquivo `.tar.gz` que podem ser distribuídos ou instalados em outros ambientes.

#### `make run`

Executa o pipeline ETL usando `spark-submit`. Este comando requer quatro parâmetros nomeados: `input`, `output` e `appName`. Esses parâmetros são usados para configurar o caminho dos dados de entrada e saída, o nome do aplicativo Spark.

**Parâmetros:**
- `input`: Caminho dos dados de entrada.
- `output`: Caminho dos dados de saída.
- `appName`: Nome do aplicativo Spark.

Se algum desses parâmetros não for fornecido, o comando será interrompido com uma mensagem de erro.

**Exemplo de Uso:**

```bash
make run input=/caminho/para/input-data/*.json output=/caminho/para/output-data appName=MyAppName master=local
```

Esse comando executará as seguintes etapas:

1. Realizará o build do pacote utilizando o comando `poetry build`.
2. Executará o `spark-submit` com os parâmetros especificados, incluindo:
   - `input`: caminho dos dados de entrada.
   - `output`: caminho dos dados de saída.
   - `appName`: nome do aplicativo Spark.

#### `make clean`

Remove arquivos temporários gerados durante o processo de build ou execução do projeto, como:

- Diretórios `dist/` e `build/`
- Diretórios de cache Python como `__pycache__/`

Este comando é útil para garantir que o ambiente esteja limpo antes de executar novas builds ou testes.

#### `make help`

Lista todos os comandos disponíveis no `Makefile` com uma breve descrição de cada um, para ajudar a entender como utilizá-los.

---

### Exemplo de Uso

1. Para configurar o ambiente de desenvolvimento, execute:

   ```bash
   make setup
   ```

2. Para instalar as dependências, execute:

   ```bash
   make install
   ```

3. Para executar os testes:

   ```bash
   make test
   ```

4. Para realizar o build do pacote:

   ```bash
   make build
   ```

5. Para executar o pipeline ETL:

   ```bash
   make run input="/caminho/para/input-data/*.json" output="/caminho/para/output-data" appName="MyAppName"
   ```

6. Para limpar os arquivos temporários gerados:

   ```bash
   make clean
   ```
