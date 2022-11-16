# Seazone Desafio

## Introdução

O presente repositório contém o código escrito para a realização do processo seletivo da empresa Seazone. Neste desafio, foi proposto a criação de uma aplicação utilizando Python, Django e um Banco de dado SQL. Minha escolha para o banco foi o PostgreSQL. A aplicação consiste num backend o qual terá 3 APIs REST.

#### Bônus
No documento do desafio não foi solicidato, porém, foi utilizado o docker para a configuração de um ambiente de desenvolvimento. O avaliador pode escolher de qual a maneira que preferir seguir. O passo a passo de como rodar a aplicação (em modo de desenvolvimento) estará totalmente destrinchado ao final deste README. [Ir direto para o Docker](#modo-desenvolvimento---docker)

## Modo desenvolvimento - Padrão

### 1. Preparando o ambiente

Primeiramente, devemos instalar na máquina algum gerenciador de pacote do python (o utilizado por mim foi o miniconda). Além disso, deve-se instalar, também, o PostgreSQL.
###### OBS: Não está no presente escopo, mostrar a instalação de um gerenciador de pacote nem do postgresql

Com o gerenciador instalado e configurado, podemos agora instalar as dependências necessárias para nossa aplicação. Pelo terminal, executamos:

``` sh
# ative seu ambiente virtual previamente
python -m pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install psycopg2
```

### 2. Configurando o PostgreSQL
Devemos configurar algumas coisas dentro do PostgreSQL para que o Django funcione corretamente.

Para isso, entre dentro do CLI do Postgre, no terminal:
``` sh
psql -U psql
```

Agora dentro da linha de comando do psql, rodamos os seguintes comandos:

```sql
-- Criamos um usário
CREATE USER khanto_user;

-- Definimos usa senha para ele
ALTER USER khanto_user WITH PASSWORD 'Abcd123*';

-- Define a codificação utilizada no tráfego com o cliente
ALTER ROLE khanto_user SET client_encoding TO 'utf8';

-- https://www.postgresql.org/docs/12/transaction-iso.html
ALTER ROLE ${KHANTO_USER} SET default_transaction_isolation TO 'read committed';

-- Utilizar horário UTC ao invés do horário brasileiro
ALTER ROLE khanto_user SET timezone TO 'UTC';

-- Cria o Banco de Dados
CREATE DATABASE khantodb;

-- Dá privilégios no banco para o usuário do sistema
GRANT ALL PRIVILEGES ON DATABASE khantodb TO khanto_user;
```

Esses comandos servem para realizar a conexão do Django com o banco de dados

### 3. Configurando o Django

Com os parâmetros criados no passo anterior, realizamos agora a conexão com o banco. Ajuste o arquivo colocando os mesmos nomes dados no passo anterior.

```py
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'khantodb',
        'USER': 'khanto_user',
        'PASSWORD': 'Abcd123*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
###### OBS: o parâmetro HOST, no repostório está como 'db' pois está configurado para o d

Com a conexão estabelecida, podemos agora fazer as migrações para o banco e carregar alguns dados.

###### OBS: as fixtures se encontram em backend/khanto/fixtures/data.json

```py
# Realiza a migração da estrutura do banco
python manage.py migrate

# Realizar a importação dos dados
python manage.py loaddata
```

### 4. Executando a aplicação

Após os passos anteriores, o Django deverá estar pronto para ser executado.

```
python manage.py runserver
```

Para verificar que tudo está correto, acesse http://localhost:8000/api/. Deverá aparecer uma lista com os 3 endpoints.

### 5. Testes

Com a aplicação rodando, os teste poderão ser tanto realizados pela interface provida pelo Django RestFramework quanto pelos teste unitários escritos.

Para rodar os testes unitários, basta:

```sh
python manage.py test
```

## Modo desenvolvimento - Docker

### 1. Configurando o Django

Como o repositório está com parâmetros para a execução do modo normal.

É **necessariamente obrigatório** mudar a configuração da conexão com o banco no settings.py. 

Deve-se alterar **somente** o parâmetro HOST para 'db'.

```py
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'khantodb',
        'USER': 'khanto_user',
        'PASSWORD': 'Abcd123*',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

### 2. Executando a aplicação

Para rodar a aplicação com o docker é bem simples. Primeiramente, iremos ao diretório onde temos os arquivos do Docker

```sh
cd dev
```

Em seguida, basta rodas:

```sh
docker-compose build
docker-compose up -d
docker-compose down # para matar os contêineres
```

Devemos também realizar as migrações e a importação dos dados.

```sh
# Entramos no bash do contêiner do django
docker exec -it django bash

# Realiza a migração da estrutura do banco
/opt/conda/envs/seazone/bin/python manage.py migrate

# Realizar a importação dos dados
/opt/conda/envs/seazone/bin/python manage.py loaddata

```

Após os passos anteriores, o Django deverá estar pronto para ser executado.

```
python manage.py runserver
```

Para verificar que tudo está correto, acesse http://localhost:8000/api/. Deverá aparecer uma lista com os 3 endpoints.

### 3. Testes

Com a aplicação rodando, os teste poderão ser tanto realizados pela interface provida pelo Django RestFramework quanto pelos teste unitários escritos.

Para rodar os testes unitários, temos que entrar no bash do contêiner e rodar:

```sh
# Entramos no bash do contêiner do django
docker exec -it django bash

# Executa os testes
/opt/conda/envs/seazone/bin/python python manage.py test
```
