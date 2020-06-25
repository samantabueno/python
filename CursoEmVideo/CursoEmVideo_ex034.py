#Programa para saber o novo salário depois de receber um aumento.

salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    aumento_pc = 10
else:
    aumento_pc = 15

novo_salario = float(salario + (salario * aumento_pc / 100))
print('Seu novo salário é {:.2f}.'.format(novo_salario))