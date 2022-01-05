# FROM dlang2/dmd-ubuntu:latest
FROM dlang2/ldc-ubuntu
LABEL Description="Vibed"

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apt update 
RUN apt install -y openssl
RUN apt install -y git

COPY . .

RUN dub
# RUN dub run -v



# github.com/wilzbach/dlang-docker
# docker pull dlangchina/dlang-gdc