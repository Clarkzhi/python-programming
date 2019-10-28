awesome_string = 'Python Programming at General Assembly is Awesome!!'

new_string = ''
for character in awesome_string:
    if character == ' ' and character != 's' and character != 'm':
        new_string += character

print(new_string)