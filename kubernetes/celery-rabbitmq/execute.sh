#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

kubectl create -f $DIR/rabbitmq-service.yaml
kubectl create -f $DIR/flower-service.yaml

kubectl create -f $DIR/rabbitmq-controller.yaml
kubectl create -f $DIR/celery-controller.yaml
kubectl create -f $DIR/flower-controller.yaml


