# Nome do pacote
PACKAGE_NAME=etl-spark

# Comando para instalar as dependências usando Poetry
install:
	poetry install

# Comando para rodar os testes com pytest
test:
	poetry run pytest tests/

# Comando para buildar o pacote utilizando Poetry
build:
	poetry build

# Comando para configurar o ambiente e instalar as dependências
setup:
	@echo "Tornando setup.sh executável..."
	chmod +x setup/setup.sh
	@echo "Executando setup.sh..."
	bash setup/setup.sh
	@echo "Executando make install..."
	$(MAKE) install

# Comando para executar o spark-submit com três parâmetros nomeados
run:
	@if [ -z "$(input)" ] || [ -z "$(output)" ] || [ -z "$(appName)" ] ; then \
		echo "Por favor, forneça os parâmetros 'input', 'output', 'appName' para este comando."; \
		exit 1; \
	fi
	poetry build && poetry run spark-submit \
		--master local  \
		--py-files "dist/$(PACKAGE_NAME)-*.whl" \
		app/main.py \
		$(input) \
		$(output) \
		$(appName)

# Comando para limpar arquivos gerados (builds, caches, etc.)
clean:
	rm -rf dist/ build/ __pycache__/

# Ajuda para listar os comandos disponíveis
help:
	@echo "Comandos disponíveis:"
	@echo "  install  - Instala as dependências do projeto"
	@echo "  test     - Executa os testes unitários"
	@echo "  build    - Constrói o pacote distribuível"
	@echo "  setup    - Verifica e cria as pastas necessárias, instala o Poetry e as dependências"
	@echo "  run      - Executa o pipeline ETL usando spark-submit com os parâmetros 'input', 'output', 'appName' e 'master'"
	@echo "  clean    - Remove arquivos gerados (builds, caches)"
