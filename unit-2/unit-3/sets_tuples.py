#sets do not allow duplicates

rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

print(type(rainbow_colors))

values = [1, 5, 7, 3, 5, 5, 9, 7]

unique_values = set(values)

print(unique_values)

#added a value to a set
unique_values.add(5)

#remove a value from a set
unique_values.remove(3)

print(unique_values)

#unique_values.remove(3) #erro if we try to remove an item that is not in set

#single lines is_isogram

def is_isogram(string):
    '''unique = set(string)
    if len(unique) == len(string):
        return True
    else:
        return False
    '''
    return len(set(string)) == len(string)     

#tuples are immutable

weekdays = ('monday', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

#weekdays(6) = 'dom'(不能改变在tuples里)

print(weekdays[0])




