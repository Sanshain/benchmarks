import asyncio
import sys

import aioredis

from utils import async_benchmark, default_times, benchmark, get_argv_dict

argv = get_argv_dict()
print(argv)

loop = asyncio.get_event_loop()
url = argv.get('-h', '192.168.99.101')
port = argv.get('-p', 6379)


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
    connection.close()


@benchmark
def main():
    if '-n' in sys.argv:
        _index = sys.argv.index('-n')
        if len(sys.argv) > _index + 1 and sys.argv[_index + 1].isdigit():
            n = int(sys.argv[_index + 1])
            loop.run_until_complete(test(n))
    else:
        coroutines = [
            test(argv.get('-j', 1000)) for i in range(argv.get('-i', 10))  # 1920 req/sec
            # test(n=3333),
            # test(n=3333),
            # test(n=3334),
        ]
        loop.run_until_complete(
            asyncio.wait(coroutines)        # 4250 req/sec from linux
                                            # 1553 req/sec from linux (10x1000)
                                            # 1400 req/sec from linux (1x5000)
                                            # 1889 req/sec from linux (20x500)
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
