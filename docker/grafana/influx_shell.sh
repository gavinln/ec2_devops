#!/bin/bash

INFLUX_DOCKER=$(docker ps -q -f "name=grafana_influxdb_1")
if [ -z "$INFLUX_DOCKER" ]; then
    echo "No docker influxdb container running"
    exit 1
fi

docker exec -t -i $INFLUX_DOCKER /opt/influxdb/influx
