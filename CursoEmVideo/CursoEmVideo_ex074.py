from random import randint

numbers = (randint(0, 100), randint(0, 100), randint(0, 100)
           , randint(0, 100), randint(0, 100))

ordered = sorted(numbers)
print(ordered)
print(f'The bigger is {ordered[-1]}, and the smaller is {ordered[0]}.')

#teachers resolution
print(f'The bigger is {max(numbers)}, and the smaller is {min(numbers)}.')


