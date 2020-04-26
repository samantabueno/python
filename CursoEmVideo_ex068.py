#Exercise to training repetition structure 'while with break'
#Game of even or odd numbers: Type a number until to loose

import random
from time import sleep

count = 0

while True:
    x = random.randint(0, 10)
    t = int(input('Type a number: '))
    n = int(input('Even or Odd number?[0/1] '))
    r = (t + x) % 2
    if r == 0:
        p = 0
    else:
        p = 1
    if p == n:
        count += 1
        print('Computer thought: ', x)
        print(f'{x} + {t} = {t + x}, and this number is {p}')
        print('You won. Lets continue ..')
        sleep(1)
    elif n not in (0, 1):
        print('Invalid Option!')
    else:
        print('Computer thought: ', x)
        print(f'{x} + {t} = {t + x}, and this number is {p}')
        print('You lose =( Game over. You won {} times.'.format(count))
        break
