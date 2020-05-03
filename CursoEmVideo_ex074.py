import random

numbers = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
           , random.randint(0, 100), random.randint(0, 100))

ordered = sorted(numbers)
print(ordered)
print(f'The bigger is {ordered[-1]}, and the smaller is {ordered[0]}.')

