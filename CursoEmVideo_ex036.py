#Program to approve or to deny a real estate credit

value_house = float(input('How much is the house? '))
salary = float(input('How much is buyer''s salary? '))
years = float(input('In how many years do you wanna pay? '))

thirty = salary * 0.3;
portion = value_house / (years * 12);

if portion > thirty:
    print('Real estate credit DENIED!!' )
    print('The portion was {:.2f} per month.'.format(portion))
else:
    print('Congratulations! Real estate credit APPROVED!!.')
    print('You will pay {:.2f} per month.'.format(portion))