#Program to transform integer numbers for (1) binary numbers, (2) octal numbers or (3) hexadecimal numbers.

number = int(input('Type a number: '))
print('Choose a option to transform: ')
print('1 - To transform for Binary number.')
print('2 - To transform for Octal number.')
print('3 - To transform for Hexadecimal number.')
option = int(input('Type your choose: '))

if option == 1:
    print('The number {} in Binary number is: {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('The number {} in Octal number is: {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('The number {} in Hexadecimal number is: {}'.format(number, hex(number)[2:]))
else:
    print('Invalid option.')
