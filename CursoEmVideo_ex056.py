# Exercice to training repetition structure (for)
# In this program the user will type name, age and genre of 4 people
# And the program will return their middle age, which man is older and how many women are under 20 years old

sum_age = 0
older_man_age = 0
older_man_name = ''
count_woman = 0

print('Type the data of four people: ')
for i in range(0, 4):
    name = str(input('Name {}:'.format(i + 1)))
    age = int(input('Age {}: '.format(i + 1)))
    sex = str(input('F/M: ')).upper()

    while sex not in ('F', 'M'):
        sex = str(input('F/M: ')).upper()

    sum_age = sum_age + age
    if age > older_man_age and sex == 'M':
        older_man_age = age
        older_man_name = name

    if age < 20 and sex == 'F':
        count_woman = count_woman + 1

print('Middle age: ', sum_age / (i + 1))
print('Older Man: ', older_man_name)
print('There are {} woman/women under 20 years old.'.format(count_woman))