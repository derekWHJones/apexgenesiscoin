#!/bin/bash

apexgenesiscoind --daemon --addresstype=legacy --changetype=legacy
until apexgenesiscoin-cli help
do
  echo "Waiting for wallet to startup"
done
./docker/main/loadwallets.sh
./docker/main/mining.sh