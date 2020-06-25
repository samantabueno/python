import random
from time import sleep
print('='*40)
print('Vamos brincar? Vou pensar em um numero, tente adivinhar!!')
n1 = int(input('Digite um numero: '))
print('PROCESSANDO ...')
sleep(3)
n2 = random.randint(0,5)
if n1 == n2:
    print('PARABENS, VC ACERTOU')
else:
    print('VOCE ERROU! O numero era: ', n2)
