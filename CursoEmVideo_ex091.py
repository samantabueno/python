from random import randint
from time import sleep
from operator import itemgetter

game = {'Player1': randint(1, 6),
        'Player2': randint(1, 6),
        'Player3': randint(1, 6),
        'Player4': randint(1, 6)}

for key, value in game.items():
    print(f'The player {key} get the number {value} in the dice.')
    sleep(1)

ranking = list()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('=-'*30)
print('-------RANKING--------')
print(ranking)

for pos, value in enumerate(ranking):
    print(f'In {pos+1} position: {value[0]} got {value[1]}')
