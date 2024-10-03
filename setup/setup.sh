#!/bin/bash

# Função para verificar e criar diretórios
create_directories() {
    echo "Verificando diretórios..."

    if [ ! -d "output" ]; then
        echo "Criando diretório 'output'..."
        mkdir -p output
    else
        echo "Diretório 'output' já existe."
    fi

    if [ ! -d "resources/input-data" ]; then
        echo "Criando diretório 'resources/input-data'..."
        mkdir -p resources/input-data
    else
        echo "Diretório 'resources/input-data' já existe."
    fi

    echo "Diretórios configurados."
}

# Função para verificar se o Poetry está instalado e instalá-lo caso não esteja
check_and_install_poetry() {
    echo "Verificando se o Poetry está instalado..."

    if ! command -v poetry &> /dev/null; then
        echo "Poetry não encontrado. Instalando..."
        curl -sSL https://install.python-poetry.org | python3 -
        echo "Poetry instalado com sucesso."
    else
        echo "Poetry já está instalado."
    fi
}

# Executa as funções
create_directories
check_and_install_poetry
