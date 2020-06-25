#Exercise to training repetition structure (while with break)
#Program to show you multiplication table of n numbers

while True:
    number = int(input('Type a number to know multiplication table: '))
    if number > 0:
        for c in range(1, 11):
            print('{} X {} = {}'.format(number, c, number*c))
    else:
        break
