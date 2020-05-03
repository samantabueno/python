#Exercise to training tuples
#Program to create a price listing

list = ('Note Book', 20, 'Pencil', 2, 'Pkg Paper', 15.5, 'Calendar', 4.5)

c = 0
print('-'*40)
print(f'{"Price Listing":^40}')
print('-'*40)
while c in range(0, len(list)):
    print(f'{list[c]:.<30}${list[c+1]:6.2f}')
    c += 2
print('-'*40)
