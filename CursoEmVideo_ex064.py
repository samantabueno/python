#Program to count and sum numbers under 999

sum = count = number = 0

while number < 999:
    number = int(input('Type a number under 999 to sum: '))
    if number < 999:
        sum += number
        count += 1
print('You typed {} numbers and the sum is {}'.format(count, sum))

#Teacher's resolution
sum = count = number = 0

number = int(input('Type a number under 999 to sum: '))
while number < 999:
    sum += number
    count += 1
    number = int(input('Type a number under 999 to sum: '))
print('You typed {} numbers and the sum is {}'.format(count, sum))

