FROM debian:bullseye-slim

EXPOSE 6379

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r -g 999 redis && useradd -r -g redis -u 999 redis


RUN apt-get update; \	
	apt-get install redis -y; \
	apt-get install host -y


COPY ./config/cluster_node/redis.conf /app/redis.conf
COPY ./start.sh /app/start.sh


# COPY ./config/cluster/systemd/cluster.service /run/systemd/system/
# COPY ./start.sh /app


WORKDIR /app

# development:

RUN apt-get install procps -y; 

CMD redis-server /app/redis.conf


# CMD ["yes", "|", "redis-server", "/app/node_1/redis.conf"]
# CMD redis-server /app/node_1/redis.conf
# WORKDIR /app/node_2
# CMD ["redis-server", "/app/node_2/redis.conf"]
# WORKDIR /app/node_3
# CMD ["redis-server", "/app/node_3/redis.conf"]

# redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002
# CMD yes yes | redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 --cluster-replicas 1

# CMD ["yes", "yes", "|", "redis-cli", "--cluster", "create", "127.0.0.1:7000", "127.0.0.1:7001", "127.0.0.1:7002"]


# CMD sleep infinity





















# *


	# 2 
	# apt-get install make gcc libc6-dev tcl; \
	# apt-get install wget; \
	# wget http://download.redis.io/redis-stable.tar.gz; \
	# tar xvzf redis-stable.tar.gz; \
	# cd redis-stable; \
	# make install; \
	# make test; \

	# check

	# redis-cli --version \
	# redis-server --version