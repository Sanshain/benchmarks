FROM alpine:3.15

LABEL Description="HAProxy"

# ENV APP_ROOT /app
# WORKDIR ${APP_ROOT}

RUN apk update && apk add haproxy


# /etc/haproxy/haproxy.cfg
COPY ./haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg


# CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
CMD haproxy -f /usr/local/etc/haproxy/haproxy.cfg
