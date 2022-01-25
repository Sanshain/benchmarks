# FROM dlang2/dmd-ubuntu:latest
# Ubuntu 18.04.5 LTS
# openssl Version: 1.1.1-1ubuntu2.1~18.04.9

# FROM alpine-ldc:1.9.0
# FROM dlang2/ldc-ubuntu
FROM dlang2/ldc-circleci
# Ubuntu 18.04.5 LTS

# curl -fsS https://dlang.org/install.sh | bash -s dmd

LABEL Description="Vibed"

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

# RUN apt update 
# RUN apt install -y openssl

RUN sudo apt update 
RUN sudo apt install -y openssl
RUN sudo apt install -y libxml2
# RUN mkdir /app/.dub/build
# RUN sudo chmod 777 /app/.dub/build

# RUN apt install -y git

COPY . .

# RUN dub
# RUN dub run -v

RUN dub upgrade

RUN sudo chmod 777 .
RUN sudo chmod 777 /app/.dub/build

# RUN dub build --compiler=dmd --build=release
RUN dub build --compiler=ldc2 --build=release


# github.com/wilzbach/dlang-docker
# docker pull dlangchina/dlang-gdc