#1. Print all the titles in the list
#2. Print all the artistes in the list
#3. Print the total play length of the playlist (can you display it in hours and minutes?)
#4. [BONUS] Can you determine the most popular genre in the list?

playlist = [{'title': 'Mercy', 'genre': 'Rock', 'artiste': 'Shawn Mendes', 'year': '2016', 'length': 3.28},
            {'title': 'Something just like this', 'genre': 'Electronic', 'artiste': 'The Chainsmokers', 'year': '2017', 'length': 4.08},
            {'title': 'Hymn For The Weekend', 'genre': 'Pop Rock', 'artiste': 'ColdPlay', 'year': '2015', 'length': 4.18},
            {'title': 'Paradise', 'genre': 'Pop Rock', 'artiste': 'Coldplay', 'year': '2011', 'length': 4.38},
            {'title': 'Viva La Vida', 'genre': 'britpop', 'artiste': 'Coldplay', 'year': '2008', 'length': 4.01},
            {'title': 'Grenade', 'genre': 'R&B', 'artiste': 'Bruno Mars', 'year': '2010', 'length': 3.41},
            {'title': 'Uptown Funk', 'genre': 'Funk', 'artiste': 'Bruno Mars', 'year': '2014', 'length': 4.30},
            {'title': 'The Hills', 'genre': 'PBR&B', 'artiste': 'The Weeknd', 'year': '2015', 'length': 4.02},
            {'title': 'Starboy', 'genre': 'Electronic', 'artiste': 'The Weeknd', 'year': '2016', 'length': 3.50},
            {'title': 'I do not care', 'genre': 'Electropop', 'artiste': 'Ed Sheeran&Justin Bieber', 'year': '2019', 'length': 3.39}]

titles = []
for title in playlist:
    if title == 'title':
        titles.append(title)
print(titles)

artistes = []
for artistes in playlist:
    if artistes == 'artiste':
        titles.append(artistes)
print(artistes)


lengthes = []
for lengthes in playlist:
    if lengthes == 'artiste':
        titles.append(lengthes):
        
        total = 0
        for num in range(len(lengthes)):
            total += lengthes[num]

print(total) 
'''

my_num = [1, 2, 4, 5, 6]

total = 0
for num in range(len(my_num)):
    total += my_num[num]
print(total)

'''