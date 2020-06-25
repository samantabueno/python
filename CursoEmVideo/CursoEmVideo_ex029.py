velocidade = int(input('Km/h: '))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite)* 7
    print ('Multa de R${},00'.format(multa))
else:
    print('OK')