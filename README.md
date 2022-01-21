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

Metric                 | errors | Requests per sec   | Requests per sec (ab)  | Requests per sec (single worker)  |
:----------------------|:------:|:------------------:|:----------------------:|:---------------------------------:|
HttpResponse		       |	0	    | 	1856 requests	   |	 1419 requests	      |		833	(888) requests			        |
render template        |	0	    | 	1346 requests	   |	 1359 requests	      |		611 (612) requests     		      |
double render template |	0	    | 	1158 requests 	 |	 1216 requests	      |		455	(482)  requests	            | 					

#### Tests with keepalive:


Metric                 | errors | Requests per sec   | Requests per sec (ab)  | Requests per sec (single worker)  |
:----------------------|:------:|:------------------:|:----------------------:|:---------------------------------:|
HttpResponse		       |	0    	| 	2839 requests	   |	 3065 requests	      |		1099 (1126) requests		        |
render template        |	0	    | 	1707 requests	   |	 1926 requests	      |		615 (649) requests     		      |
double render template |	0    	| 	1564 requests  	 |	 1577 requests	      |		498	(559)  requests	            |


* `single worker` in table head above means one worker of gunicorn (for clarity of the balancing effect)

#### Tests with wrk:

`wrk -t4 -c100 -d3s <url>`

TODO


## Another comparisions:

- from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- from [techempower](https://www.techempower.com/benchmarks/)

