# Exercise for training repetition structure
# Program that receives two numbers
# And returns a multiplication table of them

for a in range(0, 2):
    number = int(input('Type a number to know multiplication table: '))
    for c in range(1, 11):
        print('{} X {} = {}'.format(number, c, number*c))
