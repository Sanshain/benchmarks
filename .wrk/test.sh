wrk -t12 -c400 -d30s http://172.18.0.4:8000/
wrk -t4 -c100 -d3s http://172.18.0.4:8000/

# @FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd docker-machine') DO @%i