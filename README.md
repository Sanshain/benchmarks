# Benchmarks: 

Performance evaluation of various implementations for working with web sockets:

## Quick start:

#### First step:

For testing, we use a set tools (probably in the future it will be allocated to a separate repository) written specifically for load testing of websockets. It is assumed that you have **nodejs**, **npm** (or **pnpm**) and **ts-node** (or **tsc**) globally pre-installed to use them.
To get started execute following commands:

```shell
cd ./django_channels/tests
npm run i
```

#### Second step:

```
docker-compose up
```

#### Thirth step: 

```
npm run compile
# or
npm run build && npm run start
```


The following options are available for the **start** and **compile** commands:
- `-p` - address
- `-n` - requests amount
- `-c` - connections amount

For example:

```
npm run compile -- -p 8008
npm run detail -- -p 8008
```

and docker swarm: 

```
docker stack deploy -c docker-compose.yml mystack
```

****

### Configuration:

The following ports are configured by default:

- Daphne only: *8000*
- Nginx: *8008*
- HAProxy: *9000*


## Results: 

### Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available. By default 

#### Tests w/o keepalive:

Requests per sec                 | Daphne only **|   nginx balancer    | haproxy balancer         |      swarm       |
:--------------------------------|:-------------:|:-------------------:|:------------------------:|:----------------:|
400 requests via 1 connections   | 292 requests  |  285 requests       |   295 requests           |   242 requests   |
400 requests via 5 connections   | 376 requests  |  468 requests       | 503.8 requests           |   493 requests   |
400 requests via 15 connections  | 389 requests  |  668 requests       | 659.6 requests           |   692 requests   |
errors (6000 messages)           |       0       |       0             |       0                  |       0          |
100 requests via 35 connections  | 381 requests  |  667 requests       |  631 requests            |   686 requests   |
errors (3500 messages)           |       0       |       0             |       0                  |       1          |
100 requests via 100 connections | 300 requests  |  612 requests       |  603 requests            |   640 requests   |
errors ( 10000 messages)         |       2       |       0             |       0                  |       0          |
35 requests via 100 connections  | 306 requests  |  540 requests       |  575 requests            |   599 requests   |
errors ( 3500 messages)          |       0       |       0             |       1                  |       0          |
15 requests via 400 connections  | 169 requests  |  385 requests       |  385 requests            |   386 requests   |
errors ( 6000 messages)          |       7       |     3 .. 24         |        3 .. 8            |         1        |
15 requests via 400 connections *| 185 requests  |  412 requests       |  420 requests            |  425 requests    |
errors ( 6000 messages)        * |       10      |       1             |        1                 |         0        |
5 requests via 400 connections   | 156 requests  |  335 requests       |  302 requests            |   385 requests   |
errors ( 2000 messages)          |   0 .. 1      |       17            |        1 .. 16           |        30        |
5 requests via 400 connections * | 187 requests  |  401 requests       |  387 requests            | 397-436 requests |
errors ( 2000 messages)        * |       0       |       0..10         |        1 .. 16           |       0..30      |
1 requests via 400 connections * | 85 requests   |   271 requests      |   244 requests           |   247 requests   |
1 establis via 400 connections * | 124 connects  |  288 connections    |   291 connects           |  560 connects    |
errors ( 400 messages) *         |       0       |       0             |       0                  |                  |
CPU usage (max)                  |      112%     |(70..90)x4+50 = 330% | (45..85)x4 + 10% = 270 % |      374%        |
Memory usage                     |   56..124 Mb  |       215Mb         |      175Mb               |      271Mb       |
pids                             |      10       |         39          |       38                 |       45         |

**Footnotes:**

* Using `npm run detail`
* Inside `Daphne only` after up another containers performance down to 376 req/sec from 406 req/sec



### Windows 

FX-8350 && 8Gb memory is available (x64)

The following table is of exceptional value for understanding the scaling of the service depending on the hardware, no more

Requests per sec                 |  linux (VM)   |  Windows directly   |
:--------------------------------|:-------------:|:-------------------:|
400 requests via 1 connections   | 292 requests  |  395 requests       |
errors (400 messages)            |       0       |       0             |
400 requests via 5 connections   | 376 requests  |  516 requests       |
errors (2000 messages)           |       0       |       0             |
400 requests via 15 connections  | 389 requests  |  575 requests       |
errors (6000 messages)           |       0       |       0             |
100 requests via 35 connections  | 381 requests  |  520 requests       |
errors (3500 messages)           |       0       |       0             |
100 requests via 100 connections | 300 requests  |  476 requests       |
errors ( 10000 messages)         |       2       |       3             |
35 requests via 100 connections  | 306 requests  |  452 requests       |
errors ( 3500 messages)          |       0       |       0             |
15 requests via 400 connections  | 169 requests  |       -             |
errors ( 6000 messages)          |       7       |      error          |


---- 

## Another comparisions:

- frameworks from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- frameworks from [techempower](https://www.techempower.com/benchmarks/)
- frameworks from [sanshain](https://github.com/Sanshain/web_benchmarks)
- django from [sanshain](https://github.com/Sanshain/web_benchmarks/blob/django/README.md)
