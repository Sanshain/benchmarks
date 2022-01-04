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

Metric                 | Django        | Fastapi       | Express        |  Fastify *     |
:-------------         |:-------------:|:-------------:| :-------------:| :-------------:|
Request per sec        | 1514 requests | 1216 requests |  1586 requests |  1750 requests |
CPU usage (motionless) |     0.05%     | 2%            |  0%            | 0%             |
CPU usage (max)        |     390%      |      380%     |      260%      |       105%     |
Memory usage           |     220Mb     |     180Mb     |     105Mb      |      75 Mb     |
pids                   |      9        |      9-106    |      35        |       23       |
errors                 |      0        |       1       |       0 **     |        0       |

**Footnotes:**
* w/o clusterisation (manual clusterisation did not have any effect (expect the hugest memory allocation) because of (I suppose) clusterisation integrated in framework)
* w/o clusterisation was at less one error

### Windows

FX-8350 && 8Gb memory is available

#### Prepareing: 

- Apply `npm i` inside *Express* and *Fastify* directories
- Apply `pipenv shell` inside *Django* and *Fastapi* directories

Init scripts:
- **Express** *:3000*: `node index.js`
- **Fastify** *:3000*: `npm run begin`
- **Django** *:8000*:  `waitress-serve --listen=*:8000 --threads=8 project.wsgi:application` from *project* catalog
- **Fastapi** *:8000*: `uvicorn-run.bat`

Metric                 | Django (waitress) | Fastapi (just uvicorn) |    Express     | Fastify        | 
:-------------         |:-----------------:|:----------------------:| :-------------:| :-------------:|
Request per sec        | 1077 requests     |    568 (642) requests  |  2300 requests |  2300 requests  |
longest request        |      58 ms        |      113ms             |     43 ms      |      52 ms      |


Node.js clusterisation is handling via [clusters](https://www.npmjs.com/package/cluster)

