
#!/bin/bash

nohup redis-server ./node_1/redis.conf&
nohup redis-server ./node_2/redis.conf&
nohup redis-server ./node_3/redis.conf&

# sleep 5
# yes yes | redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002

# redis-server ./node_1/redis.conf
# redis-server ./node_2/redis.conf
# redis-server ./node_3/redis.conf


# for number in 1 2 3
# do
#     echo $number
#     nohup redis-server ./node_$number/redis.conf&
# done

# redis-cli -c -p 7000 