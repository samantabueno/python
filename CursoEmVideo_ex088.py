# Exercise to training lists
# Program that choose numbers for tickets for lottery

import random
from time import sleep
ticket = []
lottery = []
num = 0

q = int(input('How many tickets/plays do you want?: '))
for c in range(0, q):
    t = 0
    while t in range(0, 6):
        num = random.randint(0, 60)
        if num not in ticket:
            t += 1
            ticket.append(num)
    print(f'Ticket {c+1}: {sorted(ticket)}')
    sleep(1)
    lottery.append(ticket[:])
    ticket.clear()
print(lottery
      )

