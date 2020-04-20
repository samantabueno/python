#Game: Try to guess a number that computer selected

import random
from time import sleep
print('='*40)
print('Lets Play? Try to guess a number that I selected!!')
n1 = -1
n2 = random.randint(0, 5)
while n1 != n2:
    n1 = int(input('Type a number: '))
    print('PROCESSANDO ...')
    sleep(1)
    if n1 != n2:
        print('Its wrong! Try again!')
    else:
        print('Congratulations!')


