#Exercise to training tuples
#Program that works with tuples

tuple = (int(input('Type a number: '))
, int(input('Type other number: '))
, int(input('Type another number: '))
, int(input('Type the least number: ')))

even_numbers = ''

if 3 in tuple:
    print(f'The number 3 appears on the position {tuple.index(3)}')
else:
    print('The number 3 not appeared!')

print(f'The number 9 appeared {tuple.count(9)} times')

print('Even numbers are: ', end='')
for c in tuple:
    if c % 2 == 0:
        print(f'{c} ', end='')
