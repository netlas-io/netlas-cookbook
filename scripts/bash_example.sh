#!/usr/bin/env bash
set -euo pipefail

: "${NETLAS_API_KEY:?Set NETLAS_API_KEY to your Netlas API key}"

curl --fail --silent --show-error --max-time 30 --get \
  'https://app.netlas.io/api/domains/' \
  --data-urlencode 'q=domain:netlas.io' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $NETLAS_API_KEY" |
  jq -r '.items[0].data."@timestamp" // empty'
