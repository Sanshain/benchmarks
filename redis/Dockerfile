FROM debian:bullseye-slim

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r -g 999 redis && useradd -r -g redis -u 999 redis



RUN apt-get update; \	
	# 1 
	apt-get install redis -y
	# *

# COPY ./config/cluster/node_1 /app/node_1
# COPY ./config/cluster/node_2 /app/node_1
# COPY ./config/cluster/node_3 /app/node_3

COPY ./config/cluster /app

# COPY ./config/cluster/systemd/cluster.service /run/systemd/system/
COPY ./start.sh /app




RUN mkdir /data; \
	chown redis:redis /data;

WORKDIR /data



# development:

RUN apt-get install procps -y; 


EXPOSE 7000
# EXPOSE 6379

# WORKDIR /app/node_1
WORKDIR /app

CMD ./start.sh


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