# Exercise to training lists
# Program that receives six numbers
# And then analyse which number is the biggest and which is the smallest

list = []

for c in range(1, 6):
    list.append(int(input(f'Type a number for position {c}: ')))

maxi = max(list)
mini = min(list)
print(list)
print(f'The biggest number is {maxi} in the position is ', end='')
for pos, num in enumerate(list):
    if num == maxi:
        print(pos+1, '.. ', end='')


print(f'\nThe smallest number is {mini} in the position is ', end='')
for pos, num in enumerate(list):
    if num == mini:
        print(f'{pos+1} .. ', end='')
