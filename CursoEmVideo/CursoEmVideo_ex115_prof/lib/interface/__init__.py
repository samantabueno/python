def title(txt):
    print('-'*40)
    print(f'{txt}'.center(40))
    print('-'*40)


def readInt(msg):
    while True:
        try:
            number = int(input(msg))
        except KeyboardInterrupt:
            print('ERROR. The user did not enter a number.')
            break
        except:
            print('ERROR. Enter a integer number.')
        else:
            return number


def menu(list_):
    title('MAIN MENU')
    for k, v in enumerate(list_):
        print(f'{k+1} - {v}')
    print('-'*40)
    opc = readInt('Your option: ')
    return opc