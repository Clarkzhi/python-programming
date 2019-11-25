#problem 1:Write a function called frequency_counter that accepts a string, and returns a dictionary with the number of times each character occurs in the string
'''
def frequency_counter(string):
    frequency_counter = {}
    for letter in my_string:
        if letter in frequency_counter.items():
            frequency_counter[letter] += 1
        else:
            frequency_counter[letter] = 1
    return frequency_counter


my_string = 'hello'
frequency_counter = {}
for letter in my_string:
    if letter in frequency_counter.items():
        frequency_counter[letter] += 1
    else:
        frequency_counter[letter] = 1
print(frequency_counter)


#problem 2: Write a function called list_to_dict that accepts a person list (which is a list of lists), and returns a dictionary. Each list in the person list has only two items. The keys of your result dictionary should be the first item in each list, and the value should be the second item.
def list_to_dict(list):
    information = {'name': 'personname', 'city': 'personcity', 'job': 'personjob'}
    return information

Hero = list_to_dict('Bruce', 'Gotham City', 'Batman')
print(list_to_dict())

#1. Print all the titles in the list
#2. Print all the artistes in the list
#3. Print the total play length of the playlist (can you display it in hours and minutes?)
#4. [BONUS] Can you determine the most popular genre in the list?

'''

def frequency_counter(string):
    result = {}
    for character in string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

print(frequency_counter('happy'))


def list_to_dict(list):
    result = {}
    for item in people:
        result[item[0]] = item[1]
    return result
person = [['name', 'Alice'], ['job', 'Engineer']]
print(result)