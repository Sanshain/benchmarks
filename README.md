# Benchmarks: 

This branch is dedicated to evaluating the effectiveness of balancing and clustering with various tools:

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

Using python script (it is assumed that it is pre-installed on host machine):


```
py start.py -c 32 -r 20000 -p 8000_8001 && py start.py -c 32 -r 20000 -p 8000_8001 -t ab
py start.py -k -c 32 -r 20000 -p 8000_8001 && py start.py -k -c 32 -r 20000 -p 8000_8001 -t ab
```

Or directly:

```
loadtest -n 20000 -c 32 http://127.0.0.1:8000 && loadtest -n 20000 -c 32 http://127.0.0.1:8001
ab -n 20000 -c 32 http://127.0.0.1:8001 && ab -n 20000 -c 32 http://127.0.0.1:8001
loadtest -n 20000 -c -k 32 http://127.0.0.1:8000 && loadtest -n 20000 -c -k 32 http://127.0.0.1:8001
ab -n 20000 -c 32 -k http://127.0.0.1:8001 && ab -n 20000 -c 32 -k http://127.0.0.1:8001
```

****

### Configuration:

The following ports are configured by default:

- *8000* - apache (with mpm_events mod)
- *8008* - nginx
- *9000* - haproxy
- *9001* - just django gunicorn single worker 


## Results: 

### Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available

#### Tests w/o keepalive:

Metric                 | 1 worker      |   apache            | nginx               |      haproxy     |     swarm      |      k8s *     |
:----------------------|:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:| :-------------:|
															   short
Requests per sec       | 466 requests  | 785 requests        | 691 requests        |  1000 requests   |                |                |
Requests per sec (ab)  | 456 requests  | 849 requests        | 685 requests        |   765 requests   |                |                |
																ab 																		|
CPU usage (motionless) |     0.05%     |      2%             |        2%           |      0.15%       |       0%       |                |
CPU usage (max)        |     390%      |      380%           |      353%           |      335%        |      260%      |                |
Memory usage           |     220Mb     |      180Mb          |      175Mb          |      335Mb       |     105Mb      |                |
pids                   |      9        |      9-106          |       9             |       9          |      35        |                |
errors                 |      0        |       1             |       1             |       0          |       0 **     |                |

#### Tests with keepalive:

Metric                 | 1 worker      |   apache            | nginx               |      haproxy     |     swarm      |      k8s *     |
:----------------------|:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:| :-------------:|
Requests per sec       | 1514 requests | 1216 requests       | 1622 requests       |  1629 requests   |  1586 requests |                |
CPU usage (motionless) |     0.05%     |      2%             |        2%           |      0.15%       |       0%       |                |
CPU usage (max)        |     390%      |      380%           |      353%           |      335%        |      260%      |                |
Memory usage           |     220Mb     |      180Mb          |      175Mb          |      335Mb       |     105Mb      |                |
pids                   |      9        |      9-106          |       9             |       9          |      35        |                |
errors                 |      0        |       1             |       1             |       0          |       0 **     |                |

**Footnotes:**

#### Tests with wrk:

`wrk -t4 -c100 -d3s <url>`

*TODO*


### Windows 

FX-8350 && 8Gb memory is available (x64)

*TODO*

---- 

## Another evaluatings:

- overall from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- overall from [techempower](https://www.techempower.com/benchmarks/)
- django from [sanshain](https://github.com/Sanshain/web_benchmarks/blob/master/README.md)
