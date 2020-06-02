# Program that receives some information and put in a dictionary

person = dict()
person['Name'] = str(input('Name: '))
person['Middle'] = float(input(f'Middle of {person["Name"]}: '))
person['Status'] = 'Approved' if person['Middle'] > 6 else 'Failed'

for key, value in person.items():
    print(f'The {key} is {value}')
