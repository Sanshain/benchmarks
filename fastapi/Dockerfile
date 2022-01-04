FROM python:3.8-alpine
LABEL Description="Fastapi"

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apk update && apk add python3-dev \
						  gcc \
						  libc-dev \
						  libffi-dev
RUN apk add --no-cache bash

RUN python -m pip install --upgrade pip

RUN pip install gunicorn

COPY requirements.txt /${APP_ROOT}/requirements.txt
RUN pip install -r requirements.txt
COPY . ${APP_ROOT}
