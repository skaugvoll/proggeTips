
'''
SETUP to easily use the graphql api
we need a http request tool, lets use requests
and set the header to send json, as graphql expects json body for the query/mutation
'''
import requests

headers = {'Content-type': 'application/json'}

'''
Lets go!, first lets query all the events
'''

query = '{"query":"{tests{id}}"}'
rq = requests.post("http://localhost:5000", headers=headers, data=query)

print(rq.text)


print("\n"*3) # only for readability in terminal

'''
Then, lets mutate on of the tests
NOTICE: the \\ in the mutation, this is to escape the " characters, as they are needed to be read as string / characters and not the escape value
'''

mutation = '{ "query": "mutation { updateTest( where: {id: \\"ck365dxx7004c0899ylw6cvbl\\"}, data: {name: \\"test\\"} ) { id } }" }'
mutation = str(mutation)
rm = requests.post("http://localhost:5000", headers=headers, data=mutation)

print(rm.text)