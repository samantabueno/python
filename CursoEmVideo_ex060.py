#Exercice to training repetition structure (for and while)
#Program to calculate factorial number

number = int(input('Type a number: '))
factorial = 1
for c in range(1, number):
    if c == 1:
        factorial = number * c
    else:
        factorial = factorial * c

print('Factorial with FOR: ', factorial)


factorial2 = 1
number2 = int(input('Type a number: '))
while number2 >= 1:
    factorial2 = number2 * factorial2
    number2 = number2 - 1
print('Factorial with WHILE: ', factorial2)
