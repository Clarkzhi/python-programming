'''

#add two integers
def add(num1, num2):
    return num1 + num2


print(add(5, 10)) #pass to print function

result = add(50, 20) # assign to a variable

#function takes no arguments


#function to display hello there
def say_hello():
    print('hello There~')



#function that returns the length of a sting
def length(string):
    return len(string)

#function to return the sum of integers in a list

 def sum([1, 3, 4, 5]):
     return sum(lsit)


def sum_of_integers(a_list):
    result = 0

    for num in a_list:
        if type(num) is int:
            result += num
    

    return result

#function to reverse a string

def lalala(la_string):
    idx = 0
    while idx < len(lalala):
        print(lalala)
        idx -= 1
        


    
    return result



lalala = 'zhang li zhi shi tian cai'
idx = 5
while idx < len(lalala):
    print(lalala)
    idx += 1
    break
'''
#function to reverse a string

def rev_string(string):
    idx = len(string) - 1
    result = ''
    while idx >= 0:
        result += string[idx]
        idx -= 1
    return result

print(rev_string("Some random sting"))

#reverse string in on line (python)
def one_line_reverse(string):
    return string[::-1]

#using a for loop - Daniela's version

def daniela_reverse(string):
    result = ''
    for character in string:
        result = character + result

    return result

