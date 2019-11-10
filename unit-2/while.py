'''
#while loop is executed only when a condition is met 

import random #random number module


val = 1
while val < 10:
    print(val)
    val += 1 #increment val



#guessing game

#all keyboard input is string
#correct_answer = 7

import random

corrent_answer = random.randint(1, 10)
guess = int(input('guess my number(1 - 10) '))

while guess != corrent_answer:
    guess = int(input('wrong. try again'))

print('you are correct!!')

'''
#how do you break a loop?

name = ['jack', 'jill', 'mary', 'jane', 'kate']

idx = 0
while idx < len(name):
    if 'mary' == name[idx]:
        print('found mary!!')
        break
    idx += 1

#how do we loop forever
while True:
    answer = input('continue(y/n)' )
    if answer == 'n':
        break
