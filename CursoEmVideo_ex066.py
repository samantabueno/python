#Exercise to training repetition structure with break
#Program to count and sum numbers under 999

sum = count = 0

while True:
    number = int(input('Type a number under 999 to sum: '))
    if number == 999:
        break
    sum += number
    count += 1
print('You typed {} numbers and the sum is {}'.format(count, sum))
