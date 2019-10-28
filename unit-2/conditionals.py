total = 1

'''
if total  == 15:
    print('good')
else:
    print('bad')

if total % 2 == 0:
    print('even')
else:
    print('odd')



#comparions operators
# ==
# >
# <
# >=
# <=
# !=


#print corrsponding letter for a grade
# if score is 88 = 100 , print 'A'
# if score 68 < 79 , print 'B'
# if score 50 < 59 , print 'c'
#otherwise , print F


if total > 15:
    print('good')
elif total > 10:
    print('reasonable')
elif total > 5:
    print('bad')
else:
    print('disatrous')

score = 79
if score >= 88:
    print('A')
elif score >= 68:
    print('B')
elif score >= 50:
    print('c')
else:
    print('F')

'''

#a no empty string is 'Truthy

if "hello world" :
    print("yes , it's ture")

#an empty string is Falsey
if '':
        print('its ture')
else:
        print('it is false')

#any number that is not zero is truthy
if 13 :
    print('it is ture')

#0 is Falsey
if 0 :
    print('it is ture')
else:
    print('it is false')


a = 10
b = -11

if a > 0 or b < 0 :
    print('good')


if a > 0 and b < 0:
    print('Excennet')
else:
    print('Not good')