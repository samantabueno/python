# receber nome e peso de varias pessoas
# mostrar quantas pessoas
# lista com pessoas mais leves
# outra lista com as pessoas mais pesadas
people = []
crowd = []
lightest = 0
fattest = 0

while True:
    name = str(input('Type a name: '))
    weight = int(input('Type a weight: '))
    people.append(name)
    people.append(weight)
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
for pos, value in enumerate(crowd):
    if crowd[pos][1] == lightest:
        print(crowd[pos][0], '', end='')
print()
print(f'The people fattest weight {fattest} kilos and them names are: ', end='')
for pos, value in enumerate(crowd):
    if crowd[pos][1] == fattest:
        print(crowd[pos][0], '', end='')
print()
print(crowd)