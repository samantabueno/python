# Exercise to training lists
# Program that share even numbers and odd numbers

numbers = [[], []]

for c in range(1, 8):
    n = int(input(f'Type a {c} number: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

print('*='*20)
numbers[0].sort()
numbers[1].sort()
print('The even numbers are: ', numbers[0])
print('The odd numbers are: ', numbers[1])
print('All numbers are: ', numbers)