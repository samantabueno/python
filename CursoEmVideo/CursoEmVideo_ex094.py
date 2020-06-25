# Program that receives name, age and gender of many people
# Save all information of a person in a dictionary and all people in a list
# Show the age average, how many people were registered
# Name of all women, and a list all of people is older them average *

people = list()
age_average = sum_age = 0
person = dict()

while True:

    person['name'] = str(input('Name: '))
    while True:
        person['gender'] = str(input('M/F: ')).upper()[0]
        if person['gender'] in 'MF':
            break
    person['age'] = int(input('Age: '))

    people.append(person.copy())

    c = input('Continue? N to stop: ').upper()
    if c == 'N':
        break

print(people)
print(f' - It was registered {len(people)} people.')

for p in people:
    sum_age += p['age']
age_average = sum_age/len(people)

print(f' - The age average is {age_average}.')

print(' - The women are: ', end='')
for p in people:
    if p['gender'] == 'F':
        print(p['name'], end=' ')
print()

print(' - People list with age over the average: ')
for p in people:
    if p['age'] > age_average:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
