FROM httpd:alpine

RUN apk update && apk add procps

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf