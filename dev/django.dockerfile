FROM continuumio/miniconda3:latest

# RUN > executa o comando de criar pasta
# WORKDIR > equivalente ao comando cd
RUN mkdir -p /srv/djangoproject 
WORKDIR /srv/djangoproject

# Atualiza o container
RUN apt update -y
RUN apt upgrade -y
RUN apt install postgresql libpq-dev gcc python3-dev musl-dev -y

# Copia o arquivo de dependencias para dentro do container
COPY env.yml /srv/djangoproject/env.yml

# Atualiza alguns pacotes já instalados com o conda
RUN /opt/conda/bin/conda update -y --all

# Cria o ambiente virtual do conda
RUN /opt/conda/bin/conda env create -f env.yml

# Expoe porta
EXPOSE 8000

# Define o comando a ser executado assim que o container estiver rodando
CMD ["/opt/conda/envs/seazone/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
