#Programa para saber se três retas formam um triangulo.
#Treinando também a exibiçao em outras cores

lado1 = int(input('Digite o tamanho do primeiro lado de um triangulo: '))
lado2 = int(input('Digite o tamanho do segundo lado de um triangulo: '))
lado3 = int(input('Digite o tamanho do terceiro lado de um triangulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('\033[4;30;45mÉ possivel formar um triangulo!\033[m')
else:
    #print('\033[7mNão é possível formar um triangulo com {} {} e {}!\033[m'.format(lado1, lado2, lado3)) #apenas trocando
    #print('\033[7;31;44mNão é possível formar um triangulo\033[m') #invertendo as cores
    print('\033[1;31mNão é possível formar um triangulo\033[m') #vermelho negrito