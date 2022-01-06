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

#### Tests w/o keepalive:

Metric                 | Django        | Fastapi (sync)      | Fastapi (async)     | Django (meinheld) | Express (w c)  |  Fastify *     |  Fastify (w c) |
:-------------         |:-------------:|:-------------------:|:-------------------:|:----------------:| :-------------:| :-------------:| :-------------:|
Requests per sec       | 1514 requests | 1216 requests       | 1622 requests       |  1629 requests   |  1586 requests |  1750 requests |                |
CPU usage (motionless) |     0.05%     |      2%             |        2%           |      0.15%       |       0%       |       0%       |                |
CPU usage (max)        |     390%      |      380%           |      353%           |      335%        |      260%      |       105%     |                |
Memory usage           |     220Mb     |      180Mb          |      175Mb          |      335Mb       |     105Mb      |      75 Mb     |                |
pids                   |      9        |      9-106          |       9             |       9          |      35        |       23       |                |
errors                 |      0        |       1             |       1             |       0          |       0 **     |        0       |                |

#### Tests with keepalive:

Metric                 | Django        |Fastapi (sync)  | Fastapi(async) | Django (meinheld)|Express (w c)*** |Fastify (w/o c) |  Fastify (w c) |
:-------------         |:-------------:|:--------------:|:--------------:|:----------------:| :--------------:| :-------------:| :-------------:|
Requests per sec       | 1514 requests | 2114 requests  |  3569 requests |  2884 requests   |  4500 requests  |  3500 requests |  4500 requests |
CPU usage (motionless) |     0.05%     |        2%      |        2%      |      0.15%       |  0%             | 0%             |        0%      |
CPU usage (max)        |     390%      |       405%     |       380%     |      400%        |      195%       |       105%     |      212%      |
Memory usage           |     220Mb     |      175Mb     |      180Mb     |      335Mb       |      60Mb       |      75 Mb     |       477 Mb   |
pids                   |      9        |       61       |          9     |       9          |       9         |      35        |       47       |
errors                 |      0        |       0        |        0       |       0          |       0         |        0       |        0       |

**Footnotes:**
* w/o clusterisation (manual clusterisation did not have any effect (expect the hugest memory allocation) because of (I suppose) clusterisation integrated in framework)
* w/o clusterisation was at less one error
* Results with pm2 is not included, because its showed worse results on *loadtest* than on manual clusterisation tuning (1500 and 3800 r/sec suitably and 55 processes)

#### Tests with wrk:

`wrk -t4 -c100 -d3s <url>`

Metric                 | Django        |Fastapi (sync)  | Fastapi(async) | Django  (m)   | Express (w c)* |Fastify (w/o c) |  Fastify (w c) |
:-------------         |:-------------:|:--------------:|:--------------:|:-------------:| :-------------:| :-------------:| :-------------:|
Requests per sec       | 2200 requests |  3500 requests |  7000 requests | 4100 requests | 35000 requests | 10500 requests | 30000 requests |
CPU usage (max)        |     390%      |        380%    |       380%     |     390%      |      425%      |       425%     |      425%      |
Memory usage           |     220Mb     |      176 Mb    |      100Mb     |     235Mb     |     120Mb      |      75 Mb     |       420 Mb   |

* Results with pm2 is not included, because its showed worse results on loadtest than on manual clusterisation tuning (9000 r/sec)


### Windows 

FX-8350 && 8Gb memory is available (x64)

#### Prepareing: 

- Apply `npm i` inside *Express* and *Fastify* directories
- Apply `pipenv shell` inside *Django* and *Fastapi* directories
- I need *ldc2* compliler for vibe-d compilation

Init scripts:
- **Express** *:3000*: `node index.js`
- **Fastify** *:3000*: `npm run begin`
- **Django** *:8000*:  `waitress-serve --listen=*:8000 --threads=8 project.wsgi:application` from *project* catalog
- **Fastapi** *:8000*: `uvicorn-run.bat`
- **VibeD** *:8088*: `run.bat`
- **asp net** : *depends on your iis settings*

#### Results w/o keepalive:

Metric                 | Django (waitress) | Fastapi (just uvicorn) |    Express     |    ASP NET    | Fastify        |    IIS        |    vibeD      |
:-------------         |:-----------------:|:----------------------:| :-------------:|:-------------:| :-------------:|:-------------:|:-------------:|
Request per sec        | 1077 requests     |    568 (642) requests  |  2300 requests | 2205 requests |  2300 requests | 2416 requests | 2426 requests |
longest request        |      58 ms        |      113ms             |     43 ms      |    42 ms      |      52 ms     |    42 ms      |    41 ms      |


#### Results with keepalive:

Metric                 | Django (waitress) | Fastapi (just uvicorn) |  Express (pm2) |    ASP NET ** | Fastify (w c)* |    IIS        |      vibeD    |
:-------------         |:-----------------:|:----------------------:| :-------------:|:-------------:| :-------------:|:-------------:|:-------------:|
Request per sec        |        -//-       |    -//-                | 4132 requests  | 4572 requests |  5350 requests | 5000 requests | 5300 requests |
longest request        |                   |                        |      45 ms     |    53 ms      |      45 ms     |    41 ms      |    41 ms      |


* Node.js clusterisation is handling via [clusters](https://www.npmjs.com/package/cluster)
* ASP NET consumes about 150 MB of RAM in dev mode. I didn't check it after deployment, but it's unlikely anymore

---- 

## Another comparisions:

- from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- from [techempower](https://www.techempower.com/benchmarks/)
