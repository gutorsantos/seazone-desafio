FROM postgres:latest

ENV POSTGRES_USER psql
ENV POSTGRES_PASSWORD Abcd123*
ENV KHANTO_DBNAME khantodb
ENV KHANTO_USER khanto_user
ENV KHANTO_PASS Abcd123*
ENV KHANTO_SCHEMA khanto_schema

COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/

RUN apt update

EXPOSE 5432