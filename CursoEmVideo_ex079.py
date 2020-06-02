# Exercise to training lists
# Program that includes many numbers in a list if this number is not there yet

numbers = list()

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
numbers.sort()
print(numbers)
