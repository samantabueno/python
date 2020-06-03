# Program that receives name, year of birth, work card number of a person and calculate her age
# If this person have a work card number the program receive the hiring year, the salary,
# and calculate the hiring retirement year
# And them put all this information in a dictionary
# Finally it show us the dictionary

import datetime as d

current_year = int(d.datetime.now().year)

person = {'Name': str(input('Name: ')),
          'Borning Year': int(input('Borning Year: ')),
          'Work Card': int(input('Work Card Number: (0 if you do not have)'))}

person['Age'] = current_year - person['Borning Year']

if person['Work Card'] > 0:
    person['Hiring year'] = int(input('Hiring year: '))
    person['Salary'] = float(input('Salary: '))
    person['Retirement'] = person['Hiring year'] + 35 - person['Borning Year']

for key, value in person.items():
    print(f'The {key} is {value}')
