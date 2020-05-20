# Exercise to training lists
# Program to return ordered list without using sort() metod

l = []

for c in range(0, 5):
    n = int(input('Type a number: '))
    if c == 0 or n > l[-1]: #biggest of the last number of the list
        l.append(n)
        print('Add in the final list.')
    else:
        for pos, value in enumerate(l):
            if n < value:
                l.insert(pos, n)
                print(f'Added in the position {pos}.')
                break

print('--'*20)
print(f'The ordered list is {l}')
