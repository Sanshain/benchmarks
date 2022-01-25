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
- Vibe-d: *7000*
- Fastify: *9001*


## Results: 

### Linux

Tests was running on docker-machine with 4 virtual cores and 1256 MB memory available

#### Tests w/o keepalive:

Metric                 |Requests per sec       |CPU usage (motionless) |CPU usage (max)        |Memory usage           |pids                   |errors                 |
:--------------------- |:---------------------:|:---------------------:|:---------------------:|:---------------------:|:---------------------:|:--------------------- |
 Django                | 1514 requests         |     0.05%             |     390%              |     220Mb             |      9                |      0                |
 Fastapi (sync)        | 1216 requests         |      2%               |      380%             |      180Mb            |      9-106            |       1               |
 Fastapi (async)       | 1622 requests         |        2%             |      353%             |      175Mb            |       9               |       1               |
 Django (meinheld)     |  1629 requests        |      0.15%            |      335%             |      335Mb            |       9               |       0               |
 Express (w c)         |  1586 requests        |       0%              |      260%             |     105Mb             |      35               |       0 **            |
  Fastify *            |  1750 requests        |       0%              |       105%            |      75 Mb            |       23              |        0              |
  Fastify (w c)        |                       |                       |                       |                       |                       |                       |
   vibe-d (dmd) ****   | 2342 requests         |      0%               |       105%            |        33Mb           |          6            |        0              |


#### Tests with keepalive:

Metric                 |Requests per sec       |CPU usage (motionless) |CPU usage (max)        |Memory usage           |pids                   |errors                 |
:--------------------- |:---------------------:|:---------------------:|:---------------------:|:---------------------:|:---------------------:|:--------------------- |
 Django                | 1514 requests         |     0.05%             |     390%              |     220Mb             |      9                |      0                |
Fastapi (sync)         | 2114 requests         |        2%             |       405%            |      175Mb            |       61              |       0               |
 Fastapi(async)        |  3569 requests        |        2%             |       380%            |      180Mb            |          9            |        0              |
 Django (meinheld)     |  2884 requests        |      0.15%            |      400%             |      335Mb            |       9               |       0               |
Express (w c)***       |  4500 requests        |  0%                   |      195%             |      60Mb             |       9               |       0               |
Fastify (w/o c)        |  3500 requests        | 0%                    |       105%            |      75 Mb            |      35               |        0              |
  Fastify (w c)        |  4500 requests        |        0%             |      212%             |       477 Mb          |       47              |        0              |
   vibe-d (dmd) ****   | 4150 requests         |      0%               |       105%            |        33Mb           |          6            |        0              |


**Footnotes:**
* w/o clusterisation (manual clusterisation did not have any effect (expect the hugest memory allocation) because of (I suppose) clusterisation integrated in framework)
* w/o clusterisation was at less one error
* Results with pm2 is not included, because its showed worse results on *loadtest* than on manual clusterisation tuning (1500 and 3800 r/sec suitably and 55 processes)
* vibe-d was launched on only one core (w/o clusterisation)

#### Tests with wrk:

```
docker exec -it wrk bash
wrk -t4 -c100 -d3s <url>
```

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

Metric                 | Django (waitress) | Fastapi (just uvicorn) |     Express    |    ASP NET ** | Fastify *      |    IIS        |      vibeD    |
:-------------         |:-----------------:|:----------------------:| :-------------:|:-------------:| :-------------:|:-------------:|:-------------:|
Request per sec        |        -//-       |    -//-                | 4132 requests  | 4572 requests |  5350 requests | 5000 requests | 5300 requests |
longest request        |                   |                        |      45 ms     |    53 ms      |      45 ms     |    41 ms      |    41 ms      |


* With clusterisations and w/o is equals results (Node.js clusterisation is handling via [clusters](https://www.npmjs.com/package/cluster))
* ASP NET consumes about 150 MB of RAM in dev mode. I didn't check it after deployment, but it's unlikely anymore

---- 

## Another comparisions:

- from [the-benchmarker](https://github.com/the-benchmarker/web-frameworks)
- from [techempower](https://www.techempower.com/benchmarks/)

## Notes:

- **fastify_cluster** container was based on [this one](https://github.com/joseluisq/fastify-cluster-example). Thanks for [joseluisq](https://github.com/joseluisq)
