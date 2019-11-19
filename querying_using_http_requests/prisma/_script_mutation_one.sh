#!/bin/bash

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "authorization: Bearer xxx" \
  --data '{
  "query": "mutation { updateTest( where: {id: \"ck365dxx7004c0899ylw6cvbl\"}, data: {name: \"test\"} ){ id } }" }'\
  http://localhost:5000

