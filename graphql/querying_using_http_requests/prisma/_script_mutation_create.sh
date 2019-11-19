#!/bin/sh

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "authorization: Bearer xxx" \
  --data '{
  "query": "mutation { createTest(data: {name: \"test\", date: \"2019-10-19T17:44:08.878Z\"} ) { id name status date } }" }'\
  http://localhost:5000


echo Job executed