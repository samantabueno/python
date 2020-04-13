#Programa para saber se três retas formam um triangulo.

lado1 = float(input('Digite o tamanho do primeiro lado de um triangulo: '))
lado2 = float(input('Digite o tamanho do segundo lado de um triangulo: '))
lado3 = float(input('Digite o tamanho do terceiro lado de um triangulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('É possivel formar um triangulo!')
else:
    print('Não é possível formar um triangulo!')