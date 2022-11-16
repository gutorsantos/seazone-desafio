#!/bin/bash

# Interrompa imediatamente se algum comando der erro:
set -e

psql -v ON_ERROR_STOP=1 --username ${POSTGRES_USER} --dbname ${POSTGRES_DB} <<-EOSQL
    -- Cria o Banco de Dados
    CREATE DATABASE ${KHANTO_DBNAME};

    -- Cria o usuário
    CREATE USER ${KHANTO_USER};
    
    -- Define a senha
    ALTER USER ${KHANTO_USER} WITH PASSWORD '${KHANTO_PASS}';

    \connect khantodb;
    CREATE SCHEMA ${KHANTO_SCHEMA} AUTHORIZATION ${KHANTO_PASS};

    -- Define a codificação utilizada no tráfego com o cliente
    ALTER ROLE ${KHANTO_USER} SET client_encoding TO 'utf8';
    
    -- https://www.postgresql.org/docs/12/transaction-iso.html
    ALTER ROLE ${KHANTO_USER} SET default_transaction_isolation TO 'read committed';
    
    -- Utilizar horário UTC ao invés do horário brasileiro
    ALTER ROLE ${KHANTO_USER} SET timezone TO 'UTC';
EOSQL

