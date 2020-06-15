# Program that receives a name
# and returns how many times the letter A appears
# and wich position it appears in the first and last time


nome = str(input('Type your name: ')).upper().strip()
print('In your name, the letter A appears {} times.'.format(nome.count('A')))
print('The first time it appears is in the position {}.'.format(nome.find('A') + 1))
print('The last time it appears is in the position {}.'.format(nome.rfind('A') + 1))

