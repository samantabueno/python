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
