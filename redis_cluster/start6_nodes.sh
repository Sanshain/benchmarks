#! /bin/bash

nohup redis-server /app/redis.conf&

sleep 5


declare -a hosts

for number in 0 1 2 3 4
do
    # echo $number
    hosts[$number]=`host redis_node_$number | grep -oP '\d+\.\d+\.\d+\.\d+'`
    echo ${hosts[$number]}
done

# redis_node_0=`host redis_node_0 | grep -oP '\d+\.\d+\.\d+\.\d+'`
# redis_node_1=`host redis_node_1 | grep -oP '\d+\.\d+\.\d+\.\d+'`
# redis_cluster=`host redis_cluster | grep -oP '\d+\.\d+\.\d+\.\d+'`
# echo $redis_cluster

# yes yes | redis-cli --cluster create $redis_node_0:6379 $redis_node_1:6379 $redis_cluster:6379
# yes yes | redis-cli --cluster create ${hosts[0]}:6379 ${hosts[1]}:6379 $redis_cluster:6379

yes yes | redis-cli --cluster create ${hosts[0]}:6379 ${hosts[1]}:6379 ${hosts[2]}:6379 ${hosts[3]}:6379 ${hosts[4]}:6379 127.0.0.1:6379

# yes yes | redis-cli --cluster create ${hosts[0]}:6379 ${hosts[1]}:6379 ${hosts[2]}:6379 ${hosts[3]}:6379 ${hosts[4]}:6379 127.0.0.1:6379 --cluster-replicas 1


# yes yes | redis-cli --cluster create redis_node_0:7000 redis_node_1:7001 redis_cluster:7002

# redis-cli -c -p 7000 

# ERR Invalid node address specified: redis_node_0:6379
# https://github.com/redis/redis/issues/2410


# host ya.ru 2>/dev/null | grep -oP '\d+\.\d+\.\d+\.\d+'