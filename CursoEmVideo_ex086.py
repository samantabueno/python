# Exercise to training lists
# Program that creates 3x3 matrix

matrix = [[], [], []]
for c in range(0, 3):
    for a in range(0, 3):
        n = int(input(f'Type a number for position [{c},{a}]: '))
        matrix[c].append(n)

for pos, value in enumerate(matrix):
    for a in matrix[pos]:
        print(f'[ {a} ]', end='')
    print()