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

def readFloat(msg):
    while True:
        try:
            number = float(input(msg))
        except:
            print('ERROR. Enter a float number.')
        else:
            return number


# Main Program
number_int = str(readInt('Enter a integer number: '))
number_float = str(readFloat('Enter a float number: '))
print(f'You typed the number {number_int} and {number_float}.')


