# Benchmarks: 

This branch is dedicated to testing libraries for working with redis and redis-cluster. The branch contains two deployment configurations (*docker-compose.yml' and 'docker-compose-win.yml') for redis-cluster: the first is a cluster in which all redis nodes live in independent containers and are managed by docker-compose. In the case of the second option, redis cluster will not be available under NAT network, and the first is a cluster based on a single container

## Quick start:

In addition to the **redis** and **redis cluster** images docker-compose contains the **redis_test** image. Start `docker-compose up -d` and enter inside *redis_test*:

```
docker exec -ti redis_tests_jar bash
```

This one contains the few scripts to load test using various libraries:

- `python app.py` - **redis cluster** load test for [redis-py-cluster](https://pypi.org/project/redis-py-cluster/) (sync)
- `python aioredis_tests.py` - **redis** load test for [aioredis](https://pypi.org/project/aioredis/) (async)
- `python aioredis_cluster_test.py` - **redis cluster** load test for [aioredis_cluster](https://pypi.org/project/aioredis-cluster/) (async)

### A few facts before you start:

- Libraries designed to work with redis do not know how to work with redis cluster, and vice versa.
- By deploying redis clusters in separate containers (second options), redis cluster will not be available under NAT network 
- **RedisNav** does not support working with redis cluster. Another Redis Desktop Manager supports it, but sometimes it didn't work stably
- There is issue due redis cluster for unknown reason unavailable inside internal docker-compose network from another container via `app -h redis_cluster` (acessible just using from under NAT network)

### Configuration:

The following ports are configured by default:

- 6379 - port for default redis w/o clusters
- 7000.. 7005 - redis cluster ports for separated container (to access to redis cluster specify one either of them) (docker-compose.yml)
- 7000 (..7002) - redis cluster ports for monolit container (docker-compose-win.yml)


## Results: 

The test results are not given here, because the author does not see any usefulness in them, and the absolute values on different machines will differ


---- 

## Another comparisions:

- from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- from [techempower](https://www.techempower.com/benchmarks/)
- from [sanshain](https://github.com/Sanshain/web_benchmarks)


## Alternatives:

If the performance is not good enough in all cases, you can try using [Aerospike](https://aerospike-python-client.readthedocs.io/en/latest/aerospike.html) instead of redis
