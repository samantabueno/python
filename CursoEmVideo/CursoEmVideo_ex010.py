'''
import math
base = float(input('Digite o valor da base do triangulo: '))
altura = float(input('Digite o valor da altura do triangulo: '))
print(math.sqrt(base**2+altura**2))


import cmath
n = float(input('Digite o ângulo: '))
print('Este é o coseno de {} graus: {:.2f} '.format(n, cmath.cos(n)))
print('Este é o seno de {} graus: {} '.format(n, cmath.sin(n)))
print('Este é a tangente de {} graus: {} '.format(n, cmath.tan(n)))



import random
sorteado = random.choice(['Samanta','Roberta','Simone','Lúcia'])
lista = random.sample(['Samanta','Roberta','Simone','Lúcia'], k=4)
print('Aluno sorteado :', sorteado)
print('Aluno sorteado :', lista)

'''

import pygame
