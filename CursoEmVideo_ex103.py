# Exercise for training function
# Program that receives (or not) a name of player of soccer and number of goals
# and returns a card (statement) with this information


def card(name='<unknown>', goals=0):
    print(f'A {name} scored {goals} goals.')


n = str(input('Name: '))
g = str(input('Number of goals: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    card(goals=g)
else:
    card(n, g)
