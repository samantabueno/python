#Exercise to training repetition structure 'while with break'
#Game of even or odd numbers: Type a number until to loose

import random
from time import sleep

count = 0

while True:
    x = random.randint(0, 1)
    n = int(input('Even or Odd number?[0/1] '))
    if x == n:
        count += 1
        print('You won. Lets continue ..')
        sleep(1)
    elif n not in (0, 1):
        print('Invalid Option!')
    else:
        print('You lose =( Game over. You won {} vezes.'.format(count))
        break
