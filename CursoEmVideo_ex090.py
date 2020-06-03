# Program that receives some information and put in a dictionary

person = dict()
person['Name'] = str(input('Name: '))
person['Average'] = float(input(f'Average of {person["Name"]}: '))
person['Status'] = 'Approved' if person['Average'] > 6 else 'Failed'

for key, value in person.items():
    print(f'The {key} is {value}')
