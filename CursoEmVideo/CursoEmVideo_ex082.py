# Program that receives many numbers an then
# returns a list with even numbers and other list with odd numbers.

numbers = []
even_numbers = []
odd_numbers = []

while True:
    numbers.append(int(input('Type a number: ')))
    while True:
        cont = str(input('Do you whish continue? [Y/N]: ')).upper()
        if cont in 'YN':
            break
    if cont == 'N':
        break

print('-='* 20)
print(f'Your list is {numbers}')

for value in numbers:
    if value % 2 == 0:
        even_numbers.append(value)
    else:
        odd_numbers.append(value)

print(f'The even numbers of you list are: {even_numbers}')
print(f'The odd numbers of you list are: {odd_numbers}')
