#!/bin/sh

# code goes here.
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "authorization: Bearer xxx" \
  --data '{
  "query": "mutation { createTest(data: {name: \"test\", date: \"2019-10-19T17:44:08.878Z\"} ) { id name status date } }" }'\
  ${PRISMA_SERVICE}:5000


echo Job executed at `date`