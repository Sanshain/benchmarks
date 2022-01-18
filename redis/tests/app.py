import sys

from rediscluster import RedisCluster

from utils import get_argv_dict, async_benchmark, default_times, benchmark

print(sys.argv)

# startup_nodes = [{"host": "127.0.0.1", "port": "7000"}, {"host": "127.0.0.1", "port": "7001"}]
startup_nodes = [
    {"host": "192.168.99.101", "port": "7000"},
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

argv = get_argv_dict()
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
