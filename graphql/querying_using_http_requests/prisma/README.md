# How to access primsa through basic http requests

This repository shows how to use curl and python to execute queries and mutation in prisma / graphql

The prisma setup is the result of following prisma.io documentation on setting up prisma with new database
**NOTICE** the prisma ports are changed from 4466 to 5000! and for my specific task I needed to have an type __Test__ with name, status, date and id.

## Setup
you need to access your prisma playground and create a few Tests

### Example of opertions to execute in playground (localhost:5000)
query tests {
  tests{
    id
    status
    name
    date
  }
}

mutation createTest {
  createTest(
    data: {
       name: "Test"
      date: "2019-10-19T17:44:08.878Z"
    }
  ) {
    id
    name
    status
    date
  }
}

mutation one {
  updateTest(where:{id: "ck365idnw00840899i7s29nfs"}, data: {name: "test"}){
    id
  }
}

## Run files
if you just want to run some of the project without docker (execute single project files)

1. install prisma client (if on mac and homebrew: `brew install prisma`)
2. `prisma deploy`
3. use `terminal` to run `.sh` files (e.g `sh _script_query.sh`)
4. use `python` with `requests` module installed to run `.py` files.

## Run sidecar project
1. install `docker`
2. install `dokcer-compose`

3. `docker-compose build`
4. `docker-compose up -d`