expression = str(input('Type an expression: '))

if expression.count('(') == expression.count(')'):
    print('Expression OK')
else:
    print('Error: Verify your expression!')
