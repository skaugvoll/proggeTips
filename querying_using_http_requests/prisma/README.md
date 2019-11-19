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

