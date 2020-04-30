#Exercise to training repetition structure while with break

sum = count_over1000 = cheaper_value = 0
cheaper_name = ''

print('***-' * 10)
print('Purchasing System - ABC Supermarket ')
print('***-' * 10)

while True:
    product = str(input('Type the products name: '))
    price = float(input('Type a price: '))

    sum += price

    if price >= 1000:
        count_over1000 += 1

    if cheaper_value == 0 or cheaper_value > price:
        cheaper_value = price
        cheaper_name = product

    while True:
        c = input('There are more products? [S/N]').upper().strip()[0]
        if c in 'SN':
            break

    if c == 'N':
        print('---' * 2, 'Total')
        print(f'Purchase total is: ${sum:.2f}')
        print(f'{count_over1000} products are over $1000.00')
        print(f'The cheaper product is {cheaper_name}')
        print('---' * 10)
        print('Completed Purchase!!')
        print('---' * 10)
        break
