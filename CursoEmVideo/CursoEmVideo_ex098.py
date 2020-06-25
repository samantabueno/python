# Program that receives start number, final number and additional number
# and return the counting from start to final number by additional number


from time import sleep


def counter(a, b, c):
    aux = a
    if c > 1:
        step_aux = c
    elif c < 1:
        step_aux = c*-1
    else:
        step_aux = 1

    print(f'Counting of {a} until {b}, {step_aux} by {step_aux}.')
    if a < b:
        while aux <= b:
            print(f'{aux} ', end='')
            sleep(0.5)
            aux += step_aux
    else:
        while aux >= b:
            print(f'{aux} ', end='')
            sleep(0.5)
            aux -= step_aux
    print()


counter(1, 10, 1)
print('---------------------------')
counter(10, 0, 2)
print('---------------------------')

print('Now, It\'s your time. ')
start = int(input('Number to start: '))
least = int(input('Least number: '))
step = int(input('Step: '))
counter(start, least, step)
