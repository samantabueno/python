def money(msg):
    var = str(input(msg)).replace(',', '.')
    while var.isalpha():
        print(f'ERROR. "{var}" is not a number. Enter a number, please!')
        var = input(msg)
    return float(var)
