from time import sleep


def title(txt):
    print('-'*40)
    print(f'{txt}'.center(40))
    print('-'*40)


def save():
    title('NEW REGISTRATION')
    while True:
        try:
            name = input('Name: ').strip()
            age = int(input('Age: '))

            file = open("people.txt", "a")
            file.write(f'{name},{age}\n')
        except Exception as error:
            print('Registration error.')
        else:
            print('Success!')
            break


def tolist():
    title('REGISTERED PEOPLE')
    file = open('people.txt', 'r')
    for person in file:
        print(f'{person.split(",")[0]:<37}{person.split(",")[1]}', end='')


def menu():
    title('MAIN MENU')
    print('1 - To list registered people')
    print('2 - To register a person')
    print('3 - To exit')
    print('-'*40)


def verify_option():
    while True:
        try:
            menu()
            opt = int(input('Enter you option: '))
        except:
            print('Invalid Option.')
        else:
            if opt in (1, 2, 3):
                if opt == 1:
                    tolist()
                elif opt == 2:
                    save()
                else:
                    title('SHUTTING DOWN...')
                    break
            else:
                print('Invalid Option.')
        sleep(2)




