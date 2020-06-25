#Programa para saber se o ano é Bissexto

import datetime
ano = int(input('Digite um ano e descubra se eh bissexto: '))
data = datetime.date(ano, 12, 31) - datetime.date(ano, 1, 1)
if data.days + 1 == 366:
    print('Bissexto')
else:
    print('Nao eh Bissexto')
