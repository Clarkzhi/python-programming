#use the requests module
import requests
import json

response = requests.get('http://statsapi.web.nhl.com/api/v1/teams')

data = response.json()
#pretty print the result
#print(json.dumps(data, indent=4))
#look at the keys on your data object

#print(data.keys())

#look at the teams object - check the type
#print(type(data['teams']))

#look at the first item in this list
print(data['teams'][0])


#pertty print
#print(json.dumps(data['teams'][0], indent=4))

#save to a file

with open('nhl.json', 'w') as nhl_file:
    nhl_file.write(json.dumps(data)) 

print("done...")
