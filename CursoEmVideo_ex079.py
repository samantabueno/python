# Exercise to training lists
# Program that includes numbers in a list

numbers = []

while True:
    n = int(input('Type a number: '))
    if n not in numbers:
        numbers.append(n)
    else:
        print('This number already exists in the list. It wont be inserted.')
    while True:
        c = input('Continue? [Y/N]').upper()
        if c in 'YN':
            break
    if c == 'N':
        break

print(sorted(numbers))
