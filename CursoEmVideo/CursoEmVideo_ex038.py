# Program for comparing two numbers
print('This program will help you to compare two numbers and to know each them is bigger.')
n1 = int(input('First number: '))
n2 = int(input('Second number: '))

if n1 == n2:
    print('The numbers are equals!')
elif n1 > n2:
    print('{} is bigger then {}.'.format(n1, n2))
else:
    print('{} is bigger then {}.'.format(n2, n1))