import json

#create a class
class Person:
    #every class must have an init method
    def __init__(self, n, a):
        #print('person object initialized')
        self.name = n
        self.age = a

    def say_hello(self):
        print('Hello my name is {} and I am {} years old'.format(self.name, self.age))

#how to instantiate a class (create an object)
p = Person("John", 35)

q = Person("Jane", 28)
print(p.name)

print(q.name)

#use a class method
p.say_hello()

print(type(p))


#create a rectangle class
#it should have a length and a width
#it should have two methods, perimeter and area

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    
    def perimeter(self): #这里的perimeter不是list is a 
        result = (x.length + x.width)*2
            
        return result
    
    def area(self):
        result = (x.length * x.width)

        return result

x = Rectangle(10, 5)

print(x.length)
print(x.width)
print(x.perimeter())#method 是个带（）的方程
print(x.area())

print('Are is {}, perimter is {}'. format(x.area(), x.perimeter()))

#create a playlist class
#the playlist has a name and a list of tracks
#each track is a dictionary , with title, artiste, length of track

#write methods to add a track, to remove a track, to shuffle the playlist
'''
class Playlist:
    def __init__(self, n , l):
        self.name = n
        self.list_tracks = l

    def track(self):
        result = [{}]
        return result

    def my_track(self):
        my_track = []
        for track in my_track:
            my_track.append({'title': 'abc', 'artiste': 'def', 'length': 231})
    
    def lala_track(self):
        lala_track = []
        for track in lala_track:
            lala_track.remove({'title': 'Something just like this', 'genre': 'Electronic', 'artiste': 'The Chainsmokers', 'year': '2017', 'length': 4.08})

    def random_track(self):
        random_track = []
        import random
        for track in random_track:

j = playlist('Mix_list', )

'''

track_file_name = 'track.json'

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
    def add_track(self, title, artist, length):
        track = {}
        track['title'] = title
        track['artist'] = artist
        track['length'] = length
        self.tracks.append(track)

    def remove_track(self, title):
        for idx in range(len(self.track)):
            if title == self.tracks[idx]['title']:
                break
        self.tracks.pop(idx)

    def save_tracks(self):

        #open file for writing
        with open(track_file_name, 'w') as track_file:
            track_file.write(json.dumps(self.tracks))

    def load_tracks(self):
        #load the data from the tracks.txt file
        with open(track_file_name, 'r') as track_file:
            data = json.load(track_file)
        #set the tracks variable to the data loaded in 
        self.tracks = data

new_playlist = Playlist('new music')

new_playlist.load_tracks()

print(new_playlist.tracks)
'''
pl = Playlist('tunes')
pl.add_track('Shape of you', 'Ed Sheearn', 3.45)
pl.add_track('Mamacita', 'Tyga, Santanta', 4.15)

pl.save_tracks()
'''
