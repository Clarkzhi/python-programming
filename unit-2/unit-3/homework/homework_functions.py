
# problem 1 :Write a function called reverse_list that accepts a list, and returns a copy of the list with the items in reverse order.

def reverse_list(my_list):
    idx = len(my_list) - 1
    result = []
    while idx >= 0:
        result += my_list[idx]
        idx -= 1
    return result


# problem 2 :Write a function called encode_string that accepts a string of letters, and returns a new string with the letters replaced with their corresponding number position in the alphabet

def encode_string(string):
    idx = len(0, 23)
    result = ()
    while idx >= 0:
        result = string(idx)
    return result


# problem 3 : Write a function called pivot_split that accepts two arguments: a list of integers and an integer, called pivot. Your function should return a new list that has two lists. The first list will have all the numbers less than the pivot, the second list will have all the numbers greater than or equal to the pivot.

def pivot_split(number_list):
    pivot = 4
    result = (list_1 = [])
    result = (list_2 = [])
    for num in number_list:
        if num >= 4:
            result = list_2
        else:
            result = list_1
    return result
