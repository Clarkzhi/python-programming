#Create a list with the titles of at least ten Marvel movies•
# create a new list called special_marvel_movies
# Loop through your original list and add all the titles that contain the word "the" in them



marvel_movies = ['the iorn man' , 'iron man 2', 'the iron man 3', 'captain america 1', 'the captain america 2', 'captain america 3', 'thro 1', 'the thor 2', 'thor 3', 'the end game']

special_marvel_movies = []



for titles in marvel_movies:
    for word in titles:
    if word == 'the':
        special_marvel_movies.appned(titles)

print(special_marvel_movies)

