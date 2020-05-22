# Exercise to training lists
# Program that creates 3x3 matrix and explore the numbers

matrix = [[], [], []]
sum_even = sum_3column = biggest_2row = 0

for c in range(0, 3):
    for a in range(0, 3):
        n = int(input(f'Type a number for position [{c},{a}]: '))
        matrix[c].append(n)
        if n % 2 == 0:
            sum_even += n
        if a == 2:
            sum_3column += n
        if c == 1: # second row
            if a == 0:
                biggest_2row = n
            elif n > biggest_2row:
                biggest_2row = n

print('-'*30)
for pos, value in enumerate(matrix):
    for a in matrix[pos]:
        print(f'[ {a} ]', end='')
    print()

print(f'The sum of even numbers is: {sum_even}.')
print(f'The sum of numbers of third column is: {sum_3column}.')
print(f'The biggest number of second row is: {biggest_2row}.')