#!/bin/bash

apexgenesiscoind --daemon --addresstype=legacy --changetype=legacy
./docker/main/mining.sh