#Inside this file, write a program that plays the following game:
# Prompt the user to enter their name, or the letter e to end the game
# Create a list with five random messages. The message could be "Youare awesome!" or "People like you are party animals, woohoo!!",or anything really!
#When the user enters their name, display one message from the list at random

'''
answer = 4
guess = int(input('Guess what number thinking of (1­-10):'))
while guess != answer:
    guess = int(input('Nope, try again'))
print("You got it!")

'''


import random

answer = 'e'

guess = input('neter your name:')


messages = ['You are awesome', 'People like you are perty animals, wiigii!!', 'You are so smart', 'how are you', 'are you ok']

while guess != answer:
    guess = random.choice(messages)
    
print('you are correct')