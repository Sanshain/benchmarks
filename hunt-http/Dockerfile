# FROM dlang2/dmd-ubuntu:latest
FROM dlang2/ldc-ubuntu
LABEL Description="Hunt"

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apt update 
RUN apt install -y git

# RUN git clone https://github.com/huntlabs/hunt-skeleton.git project

WORKDIR ${APP_ROOT}/project
COPY . .

RUN dub build 
# RUN dub run -v



# github.com/wilzbach/dlang-docker
# docker pull dlangchina/dlang-gdc