# Exercise for training functions
# Program that receives Year Of Birth
# and returns if the Vote is Prohibited, Required or Optional


def vote(year):
    from datetime import datetime
    global age
    age = datetime.now().year - year
    if age < 16:
        return 'PROHIBITED'
    elif 18 <= age < 65:
        return 'REQUIRED'
    elif 16 <= age < 18 or age >= 65:
        return 'OPTIONAL'


age = 0
year_birth = int(input('What\'s your year of birth? '))
result = vote(year_birth)

print(f'You are {age} years old. Your vote is {vote(year_birth)}.')
