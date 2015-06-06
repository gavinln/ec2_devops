#!/bin/bash

# run nginx application
kubectl run-container nginx --image=nginx --port=80

# expose nginx as a service
kubectl expose rc nginx --port=80 --public-ip=192.168.33.10
