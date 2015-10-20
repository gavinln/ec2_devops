#!/bin/bash

INFLUX_DOCKER=$(docker ps -q -f "name=grafana_influxdb_1")
if [ -z "$INFLUX_DOCKER" ]; then
    echo "No docker influxdb container running"
    exit 1
fi

echo "type Ctrl+d to exit"
echo "CREATE DATABASE site"
echo "USE site"
echo "CREATE USER grafana WITH PASSWORD 'somepassword' WITH ALL PRIVILEGES"
echo "GRANT ALL PRIVILEGES ON site TO grafana"

docker exec -t -i $INFLUX_DOCKER /opt/influxdb/influx
