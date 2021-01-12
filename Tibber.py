# Created by Daniel Nilsson
# Please use my invite-link to help me with my work, we get SEK 500 each :)
# https://tibber.com/se/invite/8af85f51
# Version 1.0
# Script to fetch yesterday cost and consumption from Tibber

import json,requests

# Tibber
token = ""
headers = { 'Authorization': 'Bearer '+token, # Tibber Token 'Content-Type': 'application/json',
  'Content-Type': 'application/json'
}

data = '{ "query": "{viewer {homes {consumption(resolution: DAILY, last: 1) {nodes {from,to,cost,consumption} } } } }" }' # asking for today's hourly prices

response = requests.post('https://api.tibber.com/v1-beta/gql', headers=headers, data=data) # make the query to Tibber
response = response._content # selecting the important data from the response
parsed = json.loads(response) # parse it so we can use it easier
jsondata = []
for data in parsed["data"]["viewer"]["homes"][0]["consumption"]["nodes"]: # go through each hour
  print(data)
