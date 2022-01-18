import asyncio
import sys

import aioredis

from utils import async_benchmark, default_times, benchmark

loop = asyncio.get_event_loop()
url = '192.168.99.101'
port = 6379


# status = await connection.execute('SET', 'p', 5)
# value = await connection.execute('get', 'p')
# connection.execute('zadd', 'ddd', '0', '0')

# @async_benchmark
async def test(n=default_times):
    """
    1250 req/sec to redis on docker 1 (from 8) core w/o clusters (6379)
    :param n:
    :return:
    """
    connection = await aioredis.create_connection((url, port))
    for i in range(n):
        status = await connection.execute('zadd', 'ddd', i, i)
        value = int(
            (await connection.execute('zscore', 'ddd', i)).decode()
        )
        if value and value % 100 == 0:
            print(value)


@benchmark
def main():
    if '-n' in sys.argv:
        _index = sys.argv.index('-n')
        if len(sys.argv) > _index + 1 and sys.argv[_index + 1].isdigit():
            n = int(sys.argv[_index + 1])
            loop.run_until_complete(test(n))
    else:
        coroutines = [
            test(1000) for i in range(10)  # 1920 req/sec
            # test(n=3333),
            # test(n=3333),
            # test(n=3334),
        ]
        loop.run_until_complete(
            asyncio.wait(coroutines)        # 4250
            # test()                        # 1250 req/sec
        )


main()

# if __name__ == "__main__":
#     loop.run_until_complete(main())


# async def main():
#
#     connection = await aioredis.create_connection((url, port))
#     status = await connection.execute('SET', 'p', 5)
#     value = await connection.execute('get', 'p')
#
#     # redis = aioredis.from_url(f"redis://{url}")
#     # await redis.set("my-key", "value")
#     # value = await redis.get("my-key")
#
#     print(value)
