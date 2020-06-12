# Exercise for training functions
# Program that receives a number and calculates the factorial number


def factorial(number, show=False):
    """
    Function to find factorial number
    :param number: The number to find factorial
    :param show: Show or not show the process
    :return: Factorial number
    """
    start = 1
    f = 1
    description = ''
    while start <= number:
        description += f'{str(start)} '
        if start != number:
            description += '* '
        else:
            description += '= '
        f *= start
        start += 1
    if show:
        print(description, end='')

    return f


n = int(input('Number: '))
s = int(input('Show the calculate 0 = No / 1 = Yes: '))

print(factorial(n, s))
