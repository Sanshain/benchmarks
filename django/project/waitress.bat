waitress-serve --listen=*:8000 --threads=8 project.wsgi:application

:: --asyncore-loop-timeout=INT
:: --asyncore-use-poll

:: https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html?highlight=threads