
'''
classmates = ['emma', 25, 'toronto' 'kyle', 27, 'hamilton']

#a dictionary is a collection of key/value pairs

student = {'name': 'Emma', 'age': 25, 'address': 'Toronto'}

#access elements in a dictionary

print(student['name'])
print(student['age'])
print(student['address'])

#a dcitionary cannot have duplicate keys
'''
#add item to a dictionary
car = {} #creates an empty dictionary

car['make'] = 'Toyota'
car['model'] = 'Prius'
car['year'] = 2019
car['color'] = 'silver'

print(car)

car['year'] = 1997 #overwrites the previous value for year

print(car)

#how do we iterate over a dictionary

for item in car:
    print(car[item]) #prints the values


#make a list of dictionaries_cars
'''

car['make'] = 'Toyota', 'BMW',  'Benz', 'Audi', 'Ferrari'
car['model'] = 'Prius', 'M3', 'C63', 'S5', '458'
car['year'] = 2019, 2018, 2017, 2015, 2015
car['color'] = 'silver', 'gold', 'black', 'yellow', 'red'

print(car)不对
'''

cars = [{'make': 'Toyota', 'model': 'Prius', 'year': 2019, 'color': 'silver'},
{'make': 'Toyota', 'model': 'Prius', 'year': 2016, 'color': 'blue'},
{'make': 'BMW', 'model': 'Prius', 'year': 2015, 'color': 'white'},
{'make': 'Benz', 'model': 'Prius', 'year': 2016, 'color': 'white'},
{'make': 'Toyota', 'model': 'Prius', 'year': 2019, 'color': 'green'}]

print(cars)
#processing a list of dictionaries
total = 0
for car in cars:
    #count how many Toyotas are there
    
    if car['make'] == 'Toyota':
        total += 1

print(total)
'''
{
  '_id':100,
  'year': 2019,
  'title': 'bodak yellow',
  'artiste': {
      'name': 'cardi b',

    }
    'track': 100,
    'title':
}

#return the frequency of each letter in the sting
frequency_counter(string)

frequency_counter('a testy line of text')
'a' : 1
' ' : 4
't' : 3
'e' : 2
's' : 1
'y' : 1
'x' : 1
'i' : 1
'n' : 1
'f' : 1
'o' : 1

#use a dictionary

'''
#how to get the keys
#use the keys method 

print(car.keys())

#how to get the values
#use the values() method

print(car.values())

#to get both keys and values
#use the items method
print(car.items())

for key , value in car. items():
    print(key, value)