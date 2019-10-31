'''
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')
print('Clark')

#the for loop
name = 'Clark'
for count in range(1, 11):
    print(name)

#print the odd numbers between 1 and 10

for num in range (1, 11):
    if num % 2 == 1:
        print(num)


#print the sum of the even numbers
total=0

for num in range (1 , 11):
    if num % 2 == 0:
       total =+ num
print(num)


print('Lizhi zhang')


#store your full name in a variables
#loop over your name
#if you find avowel, print it
#'a', 'e', 'i', 'o', 'u' - vowels

name = 'lizhi zhang'
#for each letter in my name
for letter in name:
    #if the letter is a vowel. print it
    if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u':
        print(letter)




my_number = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

smallest_num = 0

for smallest_num in my_number:
    if number < my_number:
        samllest_num = number
print(smallest_num)



my_number = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]

smallest = 0

for number in my_number:
    if number < smallest:
        smallest = number

print(smallest)


#find the average of each list, store in a new list
weights = [[50, 25, 75], [95.7, 38.3, 55.2,],[ 88, 45, 16]]

averages = []

for item in weights:

    total = 0
    for value in item:
        total += value

    averages.append(total/len(item))

print(averages)        


*
**
***
****
*****
******
*******
********
*********
**********
'''

for row in range(1, 11):
    for col in range(1, row + 1):
        print('*',  end = ' ')
    print() 

#using indexed to access list items
#use index if we need to edit items in list

#set all the negative readings to 0
readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0
print(readings)


#find the position of an item in a list
current_age = 25
ages = [15, 17, 27, 35, 12, 25, 55, 40, 31, 20]

for idx in range(len(ages)):
    if ages [idx] == current_age:
        print('25 in found at position', idx)