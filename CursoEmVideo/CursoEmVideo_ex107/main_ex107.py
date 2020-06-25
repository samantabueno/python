from CursoEmVideo.CursoEmVideo_ex107 import moeda

n = float(input('Type a number: '))

print(f'Double of {n} is {moeda.double(n)}')
print(f'Half of {n} is {moeda.half(n)}')
print(f'Increasing 10% in {n}, the result is {moeda.increase(n, 10)}')
print(f'Decreasing 20% in {n}, the result is {moeda.decrease(n, 20)}')
