FROM ubuntu:16.04

MAINTAINER "Liao Yu"

RUN (\
    echo "deb http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse" && \
    echo "deb http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse" && \
    echo "deb http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse" && \
    echo "deb http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse" \
    echo "deb-src http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse" && \
    echo "deb-src http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse" && \
    echo "deb-src http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse" && \
    echo "deb-src http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse" \
    ) > /etc/apt/sources.list

RUN apt-get -y update \
  && apt-get -y build-dep nginx \
  && rm -rf /var/lib/apt/lists/*

ENV NGINX_VERSION=1.13.1 \
    NGINX_MODULE='echo-nginx-module' \
    ECHO_NGINX_MODULE_PATH="/home/$NGINX_MODULE"

COPY nginx-$NGINX_VERSION.tar.gz /home/
COPY $NGINX_MODULE /home/

RUN cd /home \
    #git clone https://github.com/openresty/echo-nginx-module.git \
    #curl -sO http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz \
  && tar -xf nginx-$NGINX_VERSION.tar.gz \
  && cd nginx-$NGINX_VERSION \
  && ./configure --prefix=/opt/nginx --add-module=$ECHO_NGINX_MODULE_PATH \
  && make -j$(nproc) \
  && make install

ENTRYPOINT ["/opt/nginx/sbin/nginx", "-g", "daemon off;"]

# /opt/nginx/conf/nginx.conf