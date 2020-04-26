#Exercise to training repetition structure (while with break)
#Program to register people (only age and genre)
#The program returns how many people under 18 years old was registred
#And how many men was registred
#And how many women under 20 years old was registred

count_people = count_over18 = count_man = count_woman_under20 = 0

while True:
    print('---'*20)
    print('Register a person!')
    print('---'*20)
    age = int(input('Type de age: '))

    while True:
        genre = input('[F/M] :').upper()
        if genre in ('F', 'M'):
            break
        else:
            print('Invalid Option!')

    count_people += 1

    if age >= 18:
        count_over18 += 1

    if genre == 'M':
        count_man += 1
    elif genre == 'F' and age < 20:
        count_woman_under20 += 1

    while True:
        co = input('Do you wanna continue? [S/N] :').upper()
        if co in ('S', 'N'):
            break
        else:
            print('Invalid Option!')

    if co == 'N':
        print('***'*20)
        print('Registration Completed!')
        print(f'People Registered: {count_people}')
        print(f'People Over 18 years old Registered: {count_over18}')
        print(f'Men Registered: {count_man}')
        print(f'Women under 20 years old Registered: {count_woman_under20}')
        print('***'*20)
        break
