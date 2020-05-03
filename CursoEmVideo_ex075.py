n1 = int(input('Type a number: '))
n2 = int(input('Type other number: '))
n3 = int(input('Type another number: '))
n4 = int(input('Type the least number: '))

tuple = (n1, n2, n3, n4)
count9 = pos3 = 0
even_numbers = ''

for c in tuple:
    if c == 9:
        count9 += 1

if 3 in (n1, n2, n3, n4):
    print(f'The number 3 appears on the position {tuple.index(3)}')
else:
    print('The number 3 not appeared!')

if count9 == 0:
    print('The number 9 not appeared!')
else:
    print(f'The number 9 appeared {count9} times')

for c in tuple:
    if c % 2 == 0:
        even_numbers += str(c) + ' '

print(f'Even numbers are: {even_numbers}')
