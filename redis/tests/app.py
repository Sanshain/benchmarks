#!/usr/local/bin/python

import sys

from rediscluster import RedisCluster

from utils import get_argv_dict, async_benchmark, default_times, benchmark

print(sys.argv)

argv = get_argv_dict()

print(argv)

# startup_nodes = [{"host": "127.0.0.1", "port": "7000"}, {"host": "127.0.0.1", "port": "7001"}]
startup_nodes = [
    {
        "host": argv.get('-h') or "192.168.99.101",
        "port": argv.get('-p') or "7000"
    },
    # {"host": "192.168.99.101", "port": "7001"},
    # {"host": "192.168.99.101", "port": "7002"},
    # {"host": "127.0.0.1", "port": "7002"},
]
redis = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)


# rc = RedisCluster(host="127.0.0.1", port=7000, decode_responses=True)

@benchmark
def test(n=default_times):
    """
    800 req/sec to redis on docker 1 (from 8) core w/o clusters (6379)
    1600-.... req/sec to redis on docker 3 containers cluster (8 core CPU) (themselves tests running from linux docker)
    1350-1589 req/sec to redis on docker 6 containers (3+3) cluster (8 core CPU) (-//-)
    1588-1637 req/sec to redis on docker 6 master containers cluster (8 core CPU) (-//-)
    :param n:
    :return:
    """
    for i in range(n):
        redis.zadd('ddd', {i: i})
        value = redis.zscore('ddd', i)
        if value and value % 100 == 0:
            print(value)


# print(rc)
# print(rc.set("foo", "bar"))
# print(print(rc.get("foo")))

test(
    argv.get('-n', default_times)
)










# if '-n' in sys.argv:
#     _index = sys.argv.index('-n')
#     if len(sys.argv) > _index + 1 and sys.argv[_index + 1].isdigit():
#         n = int(sys.argv[_index + 1])
#         test(n)
# else:
#     test()
