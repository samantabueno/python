# quantas letras a tem no nome, qual posicao aparece primeira vez, e a ultima?
nome = str(input('Digite seu nome: ')).upper().strip()
print('Seu nome tem {} vezes a letra A.'.format(nome.count('A')))
print('A primeira vez que ela aparece é na posição {}.'.format(nome.find('A') + 1 ))
print('A primeira vez que ela aparece é na posição {}.'.format(nome.rfind('A') + 1))

