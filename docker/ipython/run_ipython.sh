#!/bin/bash

docker run -d -p 443:8888 -e "PASSWORD=MakeAPassword" -p 8000:8000 ipython/notebook
