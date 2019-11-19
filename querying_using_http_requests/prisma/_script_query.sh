#!/bin/bash

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "authorization: Bearer xxx" \
  --data '{"query":"{tests{id}}"}' \
  http://localhost:5000
