# Program that verify a math expression.
# If there are the same quantity of opened and closed parenthesis.

expression = str(input('Type an expression: '))

if expression.count('(') == expression.count(')'):
    print('Expression OK')
else:
    print('Error: Verify your expression!')
