# Exercise to training lists
# Program that share even numbers and odd numbers

numbers = [[], []]

for c in range(0, 7):
    n = int(input('Type a number: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

print('*='*20)
print('The even numbers are: ', numbers[0])
print('The odd numbers are: ', numbers[1])
print('All numbers are: ', numbers)