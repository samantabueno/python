# Exercise to training lists
# Program that receives many numbers and put in a list.
# And then analyse if there are one specific number in this list.

numbers = []

while True:
    n = int(input('Type a number: '))
    numbers.append(n)
    while True:
        cont = str(input('Continue? ..[Y/N]')).upper()
        if cont in 'YN':
            break
    if cont == 'N':
        break

print('-='*20)
print(f'It was typed {len(numbers)} numbers.')
if 5 in numbers:
    print(f'The number five was typed {numbers.count(5)} times.')
else:
    print('The number five was not typed.')

print(sorted(numbers, reverse=True))
