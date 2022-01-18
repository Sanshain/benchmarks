FROM python:3.8-slim

RUN apt-get update; \
	pip install aioredis; \
	pip install aioredis_cluster; \
	pip install redis-py-cluster;


COPY ./aioredis_cluster_test.py /app/aioredis_cluster_test.py
COPY ./aioredis_tests.py /app/aioredis_tests.py
COPY ./app.py /app/app.py
COPY ./utils.py /app/utils.py


WORKDIR /app

CMD sleep infinity


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