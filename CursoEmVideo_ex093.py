# Program that receives

goals = list()

player = {
    'name': str(input('Player name: ')),
    'soccer match': int(input('How many soccer match did he play?: '))
}

for p in range(0, player['soccer match']):
    goals.append(int(input(f'How many goals in the soccer match {p + 1}?')))

player['goals'] = goals
player['total goals'] = sum(goals)

print('--'*20)
print(player)

print('--'*20)
for key, value in player.items():
    print(f'The {key} is {value}.')

print('--'*20)
print(f'The player {player["name"]} played {player["soccer match"]} times.')
for p, i in enumerate(player["goals"]):
    print(f'  => At the soccer {p+1}, he/she did {i} goals.')
print(f'It was a total that {player["total goals"]} goals.')
