#!/bin/bash

#docker run -d --net=host --privileged gcr.io/google_containers/hyperkube:v0.14.2 /hyperkube proxy --master=http://127.0.0.1:8080 --v=2

docker run -d --net=host --privileged gcr.io/google_containers/hyperkube:v0.17.0 /hyperkube proxy --master=http://127.0.0.1:8080 --v=2
