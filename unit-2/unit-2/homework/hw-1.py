#calculate the sum of all the even numbers between 1000, and 10000

even_number_total = 0

for num in range(1000 , 10001):
    if num % 2 == 0:
        even_number_total += num
print('the sunm of even numbers between 1000 and 10000 is {}'. format(even_number_total))

#print(f'the sunm of even numbers between 1000 and 10000 is {evne_number_total}')
#print('the sunm of even numbers between 1000 and 10000 is', evne_number_total)        