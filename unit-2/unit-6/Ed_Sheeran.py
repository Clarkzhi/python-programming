import requests
import json
'''
response = requests.get('https://api.deezer.com/search?redirect_uri=http%253A%252F%252Fguardian.mashape.com%252Fcallback&q=Ed%20Sheeran&index=25')
data = response.json()

with open('Ed_Sheeran.json' , 'w') as Ed_Sheeran_file:
    Ed_Sheeran_file.write(json.dumps(data))

print("done...")
'''

with open('Ed_Sheeran.json', 'r') as Ed_Sheeran_file:
   data = json.load(Ed_Sheeran_file)


print(type(data))
print(data.keys())

ED_list = data['data']
S_list = []
for track in ED_list:
    if track['album']['title'] != 'Shape of you':
        S_list.append(track['title'])
print(S_list)
