# This program is a game
# In this game You should Try to guess the number that computer selected

import random
from time import sleep
print('='*40)
print('Lets Play? Try to guess the number that I selected!!')
n1 = -1
n2 = random.randint(0, 10)
while n1 != n2:
    n1 = int(input('Type a number: '))
    print('PROCESSING ...')
    sleep(1)
    if n1 != n2:
        print('Its wrong! Try again!')
    else:
        print('Congratulations!')


