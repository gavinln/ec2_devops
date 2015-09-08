#!/bin/bash

echo "run 'ghci' to start Haskell interpreter"
echo "type ':l lyah.hs' to load functions"
echo "type Ctrl+D to exit"

docker-compose run haskell

