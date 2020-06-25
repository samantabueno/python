def readInt(msg):
    number = input(msg)
    while not number.isnumeric():
        print('ERROR.')
        number = input(msg)
    return number


# Main Program
number = str(readInt('Type a number: '))
print(f'You typed the number {number}')
