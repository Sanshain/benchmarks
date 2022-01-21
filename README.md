# Benchmarks: 

This branch is dedicated exclusively to load testing of the django framework

## Quick start:

#### First step:

To measure performance using [loadtest](https://www.npmjs.com/package/loadtest). So install it: 

```
npm i -g loadtest
```

#### Second step:

```
docker-compose up
```

#### Thirth step: 

Using python (it is assumed that it is pre-installed on host machine):

```shell
py start.py -c 32 -r 20000 -p 8000_8001 && py start.py -c 32 -r 20000 -p 8000_8001 -t ab
py start.py -k -c 32 -r 20000 -p 8000_8001 && py start.py -k -c 32 -r 20000 -p 8000_8001 -t ab
```

Or directly:

```bash
loadtest -n 20000 -c 32 http://127.0.0.1:8000 && loadtest -n 20000 -c 32 http://127.0.0.1:8001
ab -n 20000 -c 32 http://127.0.0.1:8001 && ab -n 20000 -c 32 http://127.0.0.1:8001
loadtest -n 20000 -c -k 32 http://127.0.0.1:8000 && loadtest -n 20000 -c -k 32 http://127.0.0.1:8001
ab -n 20000 -c 32 -k http://127.0.0.1:8001 && ab -n 20000 -c 32 -k http://127.0.0.1:8001
```

****

### Configuration:

The following ports are configured by default:

- HttpResponse: *8000*
- render: *8001*


## Results: 

### Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available

#### Tests w/o keepalive:

Metric                 | HttpResponse  | render template     | render template (double render)  |
:-------------         |:-------------:|:-------------------:|:--------------------------------:|
Requests per sec (ab)  | 1419 requests | 1359 requests       |          1216 requests           |
Requests per sec       | 1856 requests | 1346 requests       |          1158 requests           |
errors                 |      0        |       0             |          		0		        |

#### Tests with keepalive:

Metric                 | HttpResponse  | render template     | render template (double render)  |
:-------------         |:-------------:|:-------------------:|:--------------------------------:|
Requests per sec (ab)  | 3065 requests | 1926 requests       |          1577 requests           |
Requests per sec       | 2839 requests | 1707 requests       |          1564 requests           |
errors                 |      0        |       0             |          		0		        |


#### Tests with wrk:

`wrk -t4 -c100 -d3s <url>`

TODO


## Another comparisions:

- from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- from [techempower](https://www.techempower.com/benchmarks/)

