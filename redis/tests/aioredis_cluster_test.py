import asyncio

import aioredis_cluster

from utils import async_benchmark, default_times, benchmark

loop = asyncio.get_event_loop()
url = '192.168.99.101'
port = 7000


# @async_benchmark
async def test(n=default_times):
    """

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
        test(1000) for i in range(10)   # 1920 req/sec
        # test(n=3333),
        # test(n=3333),
        # test(n=3334),
    ]
    loop.run_until_complete(
        asyncio.wait(coroutines)
        # test()    # 650 req/sec
    )


main()
