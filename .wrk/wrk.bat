docker run -it --rm --name wrk_test --entrypoint=/bin/sh skandyla/wrk

:: docker network ls

docker network connect pentest_default wrk_test

:: docker network inspect pentest_default
:: docker attach wrk_test