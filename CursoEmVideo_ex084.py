# Exercise to traing lists
# Program that you put people and yours weights and them it returns who is lightest and fattest

people = []
crowd = []
lightest = 0
fattest = 0

while True:
    people.append(str(input('Type a name: ')))
    people.append(float(input('Type a weight: ')))
    crowd.append(people[:])
    people.clear()
    #people.pop() limpa apenas o ultimo
    while True:
        cont = str(input('Continue:? [Y/N]')).upper()
        if cont in 'YN':
            break

    if cont == 'N':
        break

for pos, value in enumerate(crowd):
    if pos == 0:
        lightest = crowd[pos][1]
        fattest = crowd[pos][1]
    else:
        if crowd[pos][1] < lightest:
            lightest = crowd[pos][1]
        elif crowd[pos][1] > fattest:
            fattest = crowd[pos][1]

print('-='*20)
print(f'It were register {len(crowd)} people.')
print(f'The people lightest weight {lightest} kilos and them names are: ', end='')
for c in crowd:
    if c[1] == lightest:
        print(c[0], '', end='')
print()
print(f'The people fattest weight {fattest} kilos and them names are: ', end='')
for c in crowd:
    if c[1] == fattest:
        print(c[0], '', end='')
print()
print(crowd)