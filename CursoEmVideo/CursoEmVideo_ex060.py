# Exercise for training repetition structure (for and while)
# Program to calculate factorial number

from math import factorial

number = int(input('Type a number: '))

factorial1 = 1
for c in range(1, number):
    if c == 1:
        factorial1 = number * c
    else:
        factorial1 = factorial1 * c

print('Factorial with FOR: ', factorial1)

factorial2 = 1
number2 = number
while number2 >= 1:
    factorial2 = number2 * factorial2
    number2 = number2 - 1
print('Factorial with WHILE: ', factorial2)

print('Factorial with import: ', factorial(number))
