#Program to count and sum numbers under 999

sum = 0
count = 0
number = 0
while number < 999:
    number = int(input('Type a number under 999 to sum: '))
    if number < 999:
        sum = sum + number
        count = count + 1
print('You typed {} numbers, and the sum is {}'.format(count, sum))
