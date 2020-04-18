#Exercice to training repetition structure
#Program to show you multiplication table of two numbers

for a in range(0, 2):
    number = int(input('Type a number to know multiplication table: '))
    for c in range(1, 11):
        print('{} X {} = {}'.format(number, c, number*c))