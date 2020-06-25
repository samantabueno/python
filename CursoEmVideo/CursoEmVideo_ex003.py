n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a multiplicação é {}, \n a divisão é {:.10f}, \n a divisão inteira é {} \n e a exponenciação é {}.'.format(s,m,d,di,e))
print('Apenas para mostrar como nao ', end ='')
print('quebrar linha mesmo com dois prints.')
