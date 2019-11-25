'''
#how to read a file

my_file = open('lines.txt', 'r')

data = my_file.read()

my_file.close() #you should close a file after using it

print(data)

#how do we write to a file
my_file = open('lines.txt', 'w') #overwrites the contents of the file, if it exists
my_file.write('Please add this new line')
my_file.close()

#if the file doesnt exit it will be created
my_file = open('new_file.txt', 'w')
my_file.write('Lines for my new file')
my_file.close()

#to add to the end of file, use append(a)
my_file = open('new_file.txt', 'a')
my_file.write('\nNew file should have new line as well')
my_file.close()
'''
#we can use 'with' if we dont want to have to close every time
with open('lines.txt', 'r') as my_file:
    data = my_file.read()

print(data)