from CursoEmVideo.CursoEmVideo_ex108 import moeda
#Acabei fazendo o ex 109 por cima do 108

n = float(input('Type a number: '))

print(f'Double of {moeda.moeda(n)} is {moeda.double(n)}')
print(f'Half of {moeda.moeda(n)} is {moeda.half(n)}')
print(f'Increasing 10% in {moeda.moeda(n)}, the result is {moeda.increase(n, 10)}')
print(f'Decreasing 20% in {moeda.moeda(n)}, the result is {moeda.decrease(n, 20)}')


