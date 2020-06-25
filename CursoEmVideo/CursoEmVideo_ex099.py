from time import sleep


def the_biggest(*num):
    print('=-'*20)
    print('Analysing values...')
    big = 0
    print(f'The numbers are: ', end='')
    for p, v in enumerate(num):
        print(f'{v} ', end='')
        if p == 0 or v > big:
            big = v
    print(f'and amount is {len(num)}.')
    print(f'The biggest number is: {big}')
    sleep(1)


the_biggest(7, 2, 3, 4)
the_biggest(3, 4, 5)
the_biggest(20, 3)
the_biggest()
