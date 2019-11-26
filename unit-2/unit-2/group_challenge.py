'''


import random

input('select one player')

player_1total = 
player_2total = 

die_rolls = (0, 1, 2, 3, 4, 5, 6,)

H = 'switch to other'
for roll in die_rolls:
    if roll == 1 or H


    '''

import random

player_one_total = 0
player_two_total = 0

turn = 1

MAX_SCORE = 20
while True:
    choice = input('[player {}] Roll or Hold [r/h]'. format(turn))
    val = random.randint(1, 6)
    if choice == 'r':
        print('player {} rolls {}'. format(turn, val))
        if val != 1:
            if turn == 1:
                player_one_total += val
            else:
                player_two_total += val

        else:
            print('player{} loses'. format(turn))
            if turn == 1:
                player_one_total = 0
                turn =2
            else:
                player_two_total = 0
                turn = 1
    else:
        print('player{} holds'. format(turn))
        if turn == 1:
            turn == 2
        else:
            turn == 1


    #check if someone wins the game
    if player_one_total >= MAX_SCORE or player_two_total >= MAX_SCORE:
        break

if player_one_total >= MAX_SCORE:
    print('player 1 wins!!!')
else:
    print('player 2 wins!!')