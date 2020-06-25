def increase(number=0, percent=0, format_=1):
    value = number + (number * (percent/100))
    if format_ == 1:
        value = moeda(value)
    return value


def decrease(number=0, percent=0, format_=1):
    value = number - (number * (percent/100))
    if format_ == 1:
        value = moeda(value)
    return value


def double(n=0, format_=1):
    value = n * 2
    if format_ == 1:
        value = moeda(value)
    return value


def half(n=0, format_=1):
    value = n / 2
    if format_ == 1:
        value = moeda(value)
    return value


def moeda(v=0, moeda='$'):
    return f'{moeda}{v:.2f}'


def resume(number=0, inc=0, dec=0):
    print('-'*30)
    print('VALUE RESUME'.center(30))
    print('-'*30)
    print(f'{"Value analyzed":.<20}{moeda(number)}')
    print(f'{"Double":.<20}{double(number)}')
    print(f'{"Half":.<20}{half(number)}')
    print(f'{inc}% of {"Increase":.<13}{increase(number, inc)}')
    print(f'{dec}% of {"decrease":.<13}{decrease(number, dec)}')
    print('-'*30)
