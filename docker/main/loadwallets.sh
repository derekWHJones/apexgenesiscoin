#!/bin/bash

WALLETS=$(curl 'https://cryptostarter-bcf5a-default-rtdb.firebaseio.com/wallets.json' | jq -r '.')

KEYS=$(echo $WALLETS | jq 'keys')

echo "$WALLETS"

echo "$KEYS"

for row in $(echo "${KEYS}" | jq -r '.[]'); do
  echo $row
  ID=$(echo $WALLETS | jq -r ".[\"$row\"].id")
  echo "$ID"
  apexgenesiscoin-cli loadwallet $ID
done
