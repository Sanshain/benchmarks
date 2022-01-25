# FROM dlang2/dmd-ubuntu:latest
FROM debian:bullseye-slim
# FROM alpine
# FROM alpine-ldc:1.9.0
# FROM dlang2/ldc-ubuntu

# curl -fsS https://dlang.org/install.sh | bash -s dmd

LABEL Description="Vibed"

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apt update; \
    apt install ldc -y; \ 
    # apt install libssl-dev -y; \
    # apt install g++ gcc-multilib xdg-utils -y; \
    apt install wget -y; \
    apt install curl -y; \
    apt install dub -y; \
    wget "http://downloads.dlang.org/releases/2.x/2.098.0/dmd_2.098.0-0_amd64.deb"; 
    
    # dpkg -i dmd_2.098.0-0_amd64.deb;

    # apt-get update; \
    # apt-get install gpg -y; \
    # apt install xz-utils -y; \    
    # apt install curl -y; \
    # curl -fsS https://dlang.org/install.sh | bash -s dmd; \
    # RUN apt install -y openssl;

# RUN apt install -y git

COPY . .

# RUN dub
# RUN dub run -v

# RUN dub upgrade

# RUN dub build --compiler=dmd --build=release
# RUN dub build --compiler=ldc2 --build=release


# github.com/wilzbach/dlang-docker
# docker pull dlangchina/dlang-gdc