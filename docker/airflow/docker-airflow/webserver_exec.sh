#!/bin/bash

DOCKER_ID=$(docker ps -q -f name=dockerairflow_webserver)

[ -n "$DOCKER_ID" ] && docker exec -t -i $DOCKER_ID bash
