nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('Seu nome completo tem {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))