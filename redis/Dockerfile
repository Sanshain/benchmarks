FROM debian:bullseye-slim

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r -g 999 redis && useradd -r -g redis -u 999 redis



RUN apt-get update; \
	
	# 1 
	# apt-get install redis -y

	# 2 
	apt-get install make gcc libc6-dev tcl; \
	apt-get install wget; \
	wget http://download.redis.io/redis-stable.tar.gz; \
	tar xvzf redis-stable.tar.gz; \
	cd redis-stable; \
	make install; \
	make test; \

	# check

	# redis-cli --version \
	# redis-server --version

RUN mkdir /data; \
	chown redis:redis /data;

WORKDIR /data



# development:

RUN apt-get install procps -y; 



EXPOSE 6379
# CMD ["redis-server"]

CMD sleep infinity