#Greatest Common Divisor with 5 numbers

list = [30, 35, 20, 10, 5]
min = min_div = 1
new_list = sorted(list[:])
continue_divisor = ''

while new_list != [1, 1, 1, 1, 1]:
    divisible_all = True
    if 'S' not in continue_divisor:
        min += 1
    continue_divisor = ''
    for pos, value in enumerate(new_list):
        division = int(value / min)
        if value % min == 0:
            new_list[pos] = division
            # verifing if is to continue with the same 'min'
            if division % min == 0:
                continue_divisor += 'S'
            else:
                continue_divisor += 'N'
        else:
            new_list[pos] = value
            divisible_all = False
    if divisible_all:
        min_div *= min

print(f'GCD({list})= {min_div}')
