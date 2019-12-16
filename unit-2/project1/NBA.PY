import requests
import json
'''
url = "https://api-nba-v1.p.rapidapi.com/games/seasonYear/2018"

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "deadb02e20msh97a17fb6c088f0dp188313jsne087956d38a8"
    }

response = requests.request("GET", url, headers=headers)




data = response.json()
with open('NBA.json', 'w') as NBA_file:
    NBA_file.write(json.dumps(data))

print('done...')

'''
with open('NBA.json', 'r') as NBA_file:
    NBA = json.load(NBA_file)


print(type(NBA))
print(NBA.keys())

[{a:1, b:2}{ad:2, c:4}]
if ad > a 
return win




