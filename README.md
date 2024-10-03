Claro! Aqui está o `README.md` formatado em Markdown:

```markdown
# ETL com PySpark

Este projeto é uma solução de ETL (Extract, Transform, Load) utilizando PySpark. O objetivo é processar dados de viagens de táxi em Nova York, realizando agregações e transformações para extrair insights, como identificar o fornecedor com o maior número de viagens e a semana com o maior número de viagens.

## Estrutura de Pastas

A estrutura de diretórios do projeto é organizada da seguinte forma:

```

etl-spark/
├── app/
│   ├── __init__.py
│   ├── main.py                # Script principal que executa o processo de ETL
│   └── transformations.py      # Contém a classe com as transformações de dados
├── resources/
│   ├── input-data/             # Dados de entrada em formato JSON
│   └── output-data/            # Dados de saída processados
├── tests/
│   ├── __init__.py
│   ├── test_transformations.py  # Testes unitários para validação das transformações
├── dist/                       # Pacote distribuível (construído com poetry)
├── Dockerfile                  # Configuração para o container Docker
├── pyproject.toml              # Dependências do projeto gerenciadas pelo Poetry
├── README.md                   # Documentação do projeto
└── requirements.txt            # Dependências do projeto

```

## Dependências

Este projeto utiliza as seguintes bibliotecas e ferramentas:

- **Python 3.9+**
- **Apache Spark 3.2.0**
- **PySpark**
- **Poetry** (para gerenciamento de dependências)
- **pytest** (para testes unitários)
  
Instale as dependências com Poetry:

```bash
poetry install
```

Ou utilizando o `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Como Executar o Projeto

### 1. Executando com Spark-Submit

Para rodar o processo ETL via `spark-submit`, você pode utilizar o seguinte comando:

```bash
poetry build && poetry run spark-submit \
    --master local \
    --py-files dist/etl_spark-*.whl \
    app/main.py \
    /caminho/para/input-data/*.json \
    /caminho/para/output-data
```

Esse comando:
- Compila o pacote PySpark (`etl_spark-*.whl`) usando o Poetry.
- Usa o `spark-submit` para rodar o script `main.py`, que executa o pipeline de ETL.
- Processa os arquivos de entrada na pasta especificada (`input-data`) e escreve os resultados na pasta de saída (`output-data`).

### 2. Executando Testes

Os testes de unidade e integração foram implementados utilizando o framework `pytest`. Para executar os testes, utilize o seguinte comando:

```bash
poetry run pytest tests/
```

Os testes verificam as principais transformações e agregações do projeto para garantir que os resultados estejam corretos.

### 3. Docker (Opcional)

Para rodar o projeto dentro de um container Docker, você pode utilizar o `Dockerfile` incluído. Construa a imagem com o seguinte comando:

```bash
docker build -t etl-spark .
```

Depois, rode o container:

```bash
docker run --rm -v $(pwd):/app etl-spark
```

## Estrutura de Transformações

As transformações de dados estão encapsuladas na classe `TripTransformation`, localizada em `app/transformations.py`. A classe contém métodos responsáveis por adicionar colunas de ano e semana, calcular o fornecedor com mais viagens por ano, identificar a semana com mais viagens e calcular quantas viagens o fornecedor principal fez na semana principal.

O pipeline de transformação completo é executado através do método `transform()`.

## Contribuição

Se desejar contribuir para o projeto, sinta-se à vontade para abrir um Pull Request ou relatar problemas através da seção de Issues.
```

Você pode copiar e colar este texto em um arquivo `README.md` no seu projeto. Se precisar de mais ajustes, é só avisar!