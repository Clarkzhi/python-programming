import requests
import json
'''
response = requests.get('https://api.deezer.com/search?redirect_uri=http%253A%252F%252Fguardian.mashape.com%252Fcallback&q=Cardi&index=25d')
data = response.json()

with open('Cardi_B.json', 'w') as Cardi_B_file:
     Cardi_B_file.write(json.dumps(data))

print("done...")

print(type(data))
'''
with open('Cardi_B.json', 'r') as Cardi_B_file:
    data = json.load(Cardi_B_file)
print('done...')

print(type(data))
print(data.keys())