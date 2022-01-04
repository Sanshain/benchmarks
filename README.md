# Benchmarks: 

Performance comparison for **django**, **fastapi**, **express** vs **fastify**:

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

```
loadtest -n 20000 -c 32 http://127.0.0.1:8000
```

Instead of `8000` would be either port of testing framework

****

### Configuration:

The following ports are configured by default:

- Django: *8000*
- Fastapi: *8008*
- Express: *9000*
- Fastify: *9001*


## Results: 

### Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available

Metric         | Django        | Fastapi       | Express        |  Fastify *     |
:------------- | ------------- |:-------------:| :-------------:| :-------------:|
Request per sec| 1514 requests | 1216 requests |  1586 requests |  1750 requests |
CPU usage (max)|          |||105%|
Memory usage   |
pids           |
errors         |

* w/o clusterisation (manual clusterisation did not have any effect (expect the hugest memory allocation) because of (I suppose) clasterisation integrated in framework)

### Django

- waitress (Windows)
- gunicorn (Linux)

### Fastapi

- uvicorn under gunicorn (Linux)
- uvicorn w/o gunicorn (Windows)

### Express

- using node.js [clusters](https://www.npmjs.com/package/cluster)
- w/o clusters

### fastapi
- using node.js [clusters](https://www.npmjs.com/package/cluster)
- w/o clusters
