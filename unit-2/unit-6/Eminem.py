import requests
import json

'''
response = requests.get('https://api.deezer.com/search?redirect_uri=http%253A%252F%252Fguardian.mashape.com%252Fcallback&q=eminem&index=25')

data = response.json()

with open('Eminem.json', 'w') as Eminem_file:
    Eminem_file.write(json.dumps(data))

print("done...")
'''

with open('Eminem.json', 'r') as Eminem_file:
    data = json.load(Eminem_file)

print(type(data))
print(data.keys())

print(type(data['data']))

Eminem_list = data['data']
num_tracks = len(Eminem_list)
print(num_tracks)



#print(data['data'])
album_list = []
for album in Eminem_list:
    if album['album']['title'] == 'Recovery':
         album_list.append(album['title'])

print(album_list)

num_album = len(album_list)
print(num_album)


album_list_1 = []
for album['album'] in Eminem_list:
    if album['album']['title'] != 'Recovery':
         album_list_1.append(album['album']['title'])

print(album_list_1)

total = 0 
for lyrics in Eminem_list:
    if lyrics['explicit_content_lyrics'] == 1:
        total += 1
print(total)

print(album['id'])