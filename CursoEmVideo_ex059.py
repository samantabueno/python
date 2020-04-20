#Exercice to training repetition structure (while)
#Program to sum or multiply or to know which is biggest of two numbers that user type

action = 0

while action != 5:
    n1 = int(input('Type the first number: '))
    n2 = int(input('Type the second number: '))
    action = int(input('''What do you like to do: 
[1] to sum
[2] to multiply 
[3] to know which is biggest
[4] to type others numbers
[5] to exit 
'''))
    if action == 1:
        print('Sum: {} + {} = {}'.format(n1, n2, n1 + n2))
    elif action == 2:
        print('Multiplication: {} * {} = {}'.format(n1, n2, n1 * n2))
    elif action == 3:
        print('The biggest between {} and {} is {}'.format(n1, n2, max(n1, n2)))
    elif action > 5 or action < 1:
        print('Invalid option.')
