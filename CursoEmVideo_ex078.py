list = [int(input('Type a number'))
, int(input('Type other number'))
, int(input('Type another number'))
, int(input('Type another number'))
, int(input('Type last number'))]
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
        print(f'{pos+1}.. ', end='')
