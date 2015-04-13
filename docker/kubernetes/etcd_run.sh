#!/bin/bash

docker run --net=host -d kubernetes/etcd:2.0.5.1 /usr/local/bin/etcd --addr=127.0.0.1:4001 --bind-addr=0.0.0.0:4001 --data-dir=/var/etcd/data
