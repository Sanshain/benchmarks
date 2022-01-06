FROM python:3.8-alpine
LABEL Description="Django"

# EXPOSE 8000

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

RUN apk update && apk add python3-dev \
						  gcc \
						  libc-dev \
						  libffi-dev
RUN apk add --no-cache bash

RUN python -m pip install --upgrade pip

RUN apk add libev-dev
RUN apk add libwebp-dev 
RUN pip install bjoern 
RUN pip install -U meinheld 

# RUN pip install uWSGI 

COPY requirements.txt /${APP_ROOT}/requirements.txt
RUN pip install -r requirements.txt
COPY . ${APP_ROOT}

WORKDIR ${APP_ROOT}/project