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
py start.py -c 32 -r 20000 -p && py start.py -c 32 -r 20000 -p -t ab
py start.py -k -c 32 -r 20000 -p && py start.py -k -c 32 -r 20000 -p -t ab
```

Or directly:

```
loadtest -n 20000 -c 32 http://127.0.0.1:8000 && loadtest -n 20000 -c 32 http://127.0.0.1:8008
ab -n 20000 -c 32 http://127.0.0.1:8001 && ab -n 20000 -c 32 http://127.0.0.1:8008
loadtest -n 20000 -c -k 32 http://127.0.0.1:8000 && loadtest -n 20000 -c -k 32 http://127.0.0.1:8008
ab -n 20000 -c 32 -k http://127.0.0.1:8000 && ab -n 20000 -c 32 -k http://127.0.0.1:8008
```

****

### Configuration:

The following ports are configured by default:

- *8000* - apache (with mpm_events mod)
- *8008* - nginx
- *9000* - haproxy
- *9001* - just django gunicorn single worker 


# Results: 

## Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available

### Tests w/o keepalive:

#### 32 concurencies with 20000 requests:

Metric                 | 1 worker      |   apache             | nginx                  |      haproxy            |     swarm                 |
:----------------------|:-------------:|:--------------------:|:----------------------:|:-----------------------:| :-----------------------: |
Requests per sec       | 487 requests  | 785 requests         | 691 requests           |  1000 requests          |    ( 485 ..) 837          |
errors                 |      1        |       3              |       0                |         1               |    0 (..18)               |
Requests per sec (ab)  | 456 requests  | 849 requests         | 685 requests           |   765 requests          |    ( 558 ..) 1014         |
errors (ab)            |      0        |       9              |       0                |       0                 |    0                      |
CPU usage (max)        |     111%      |  80% + 4 x (45..95)% | 60..70 + 4x(50..70)%   |  4 x (65..99%) + 105%   |  4х(28..105) = 396 %      |
Memory usage           |     64Mb      | 62 + 4 х 64 = 318 Mb |   8 + 4 х 64 = 264 Mb  |    8 + 4 х 64 = 264 Mb  | 4 x (140 .. 255) = 879 Mb |
pids                   |      2        |  225 ( 217 + 2 x 4 ) |    13 ( 5 + 2 x 4 )    |     12 ( 4 + 2 x 4 )    |    9 х 4 = 36             |


#### 100 concurencies with 5000 requests:

Requests per sec       | 1 worker      |   apache            | nginx               |      haproxy     |     swarm      |
:----------------------|:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:|
Requests per sec       | 479 requests  | 955 requests        | 706 requests        |   946 requests   |     1001 req   |
errors                 |      0        |       48            |       0             |       0          |       0        |
Requests per sec (ab)  | 508 requests  | 911 requests        | 698 requests        |   936 requests   |     1020 req   |
errors (ab)            |      0        |        3            |       0             |       0          |       0        |


### Tests with keepalive:

#### 32 concurencies with 20000 requests:

Requests per sec       | 1 worker      |   apache            | nginx               |      haproxy     |     swarm      |
:----------------------|:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:|
Requests per sec       | 520 requests  | 1055 requests       | 799 requests        |   1146 requests  |      1300      |
errors                 |      0        |       1             |       0             |       0          |       0 **     |
Requests per sec (ab)  | 546 requests  | 1193 requests       | 793 requests        |   1218 requests  |      1430      |
errors (ab)            |      0        |        3            |       0             |       0          |       0        |


#### 100 concurencies with 5000 requests:

Requests per sec       | 1 worker      |   apache            | nginx               |      haproxy     |     swarm      |
:----------------------|:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:|
Requests per sec       | 524 requests  | 1069 requests       | 762 requests        |  1149 requests   |  (327..) 1185  |
errors                 |      0        |       14            |       0             |       0          |    0 (.. 7)    |
Requests per sec (ab)  | 520 requests  | 1087 requests       | 798 requests        |  1209 requests   |   (_ ..) 1312  |
errors (ab)            |      0        |        16           |       0             |       0          |       0        |


#### Tests with wrk:

`wrk -t4 -c100 -d3s <url>`

*TODO*


### Windows 

FX-8350 && 8Gb memory is available (x64)

*TODO*

---- 

**Footnotes:**

* Under loading was django unit with double template rendering
* The balancing method is used by the number of requests
* as a benchmark for evaluating the performance of the balancers, run gunicorn with 8 workers. The results of measurements for such on the tested machine: 
** 1096/1180 req/sec on 100 connections and 5000 requests - w/o keepalive
** 1150/1196 req/sec on 32 connections and 20000 requests - w/o keepalive
** 1334/1521 req/sec on 100 connections and 5000 requests - w keepalive
** 1467/1585 req/sec on 32 connections and 20000 requests - w keepalive
** loading: 405% CPU + 380 MB memory on 9 pids
** errors 0 
* swarm is the least stable: in the first test with 100 connections and 5000 requests, it just threw an error for apache benchmarks, and somehow miraculously worked only after passing other tests. When increasing the replicas to 8, he barely issued 180 req/sec for loadtest. After that, he stopped responding to the tests at all. This bugs are probably due to the configuration change in runtime, as well as the unstable state of the containers for some time after loading. In any case, after applying the scale parameter without rebooting, the containers did not work normally (the container needs to be warmed up)


## Another evaluatings:

- overall from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- overall from [techempower](https://www.techempower.com/benchmarks/)
- django from [sanshain](https://github.com/Sanshain/web_benchmarks/blob/master/README.md)
