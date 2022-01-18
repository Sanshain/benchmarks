import asyncio

import aioredis_cluster

from utils import async_benchmark, default_times, benchmark, get_argv_dict

argv = get_argv_dict()
print(argv)

loop = asyncio.get_event_loop()
url = argv.get('-h', '192.168.99.101')
port = argv.get('-p', 7000)


# @async_benchmark
async def test(n=default_times):
    """
    600-650 req/sec to redis on docker 1 (from 8) core w/o clusters (6379)
    :param n:
    :return:
    """
    redis = await aioredis_cluster.create_redis_cluster([
        (url, port),
        # (url, 7001),
        # (url, 7002),
    ])

    for i in range(n):
        status = await redis.zadd("ddd", i, i)
        value = int(
            await redis.zscore('ddd', i)
        )
        if value and value % 100 == 0:
            print(value)


@benchmark
def main():
    coroutines = [
        test(argv.get('-j', 1000)) for i in range(argv.get('-i', 10))   # 1920 req/sec (w/o clusters)
                                                                        # 1920 (not misspell) req/sec (w 3 clusters)
                                                                        # 1897 (not misspell) req/sec (w 6 clusters)
        # test(n=3333),
        # test(n=3333),
        # test(n=3334),
    ]
    loop.run_until_complete(
        asyncio.wait(coroutines)
        # test()    # 650 req/sec
    )


main()
