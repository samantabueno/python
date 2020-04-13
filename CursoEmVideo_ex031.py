distancia = int(input('Distancia viagem: '))
preco = 0.50
#50 cents ate 200 km 45 mais longas

if distancia > 200:
    preco = 0.45
print('O preco da sua passagem eh R${:.2f} '.format(distancia*preco))
