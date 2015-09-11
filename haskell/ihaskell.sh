#!/bin/bash

ip=`hostname -I | cut -f2 -d' '`
echo Connect to $ip:8778
echo The ./notebooks directory is shared
docker run -d -p 8778:8778 gregweber/ihaskell
