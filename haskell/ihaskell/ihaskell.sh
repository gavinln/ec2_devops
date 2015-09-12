#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

ip=`hostname -I | cut -f2 -d' '`
echo Connect to $ip:8778
echo The ./notebooks directory is shared

ls $DIR/notebooks
docker run -d -p 8778:8778 -v $DIR/notebooks:/notebooks ihaskell
