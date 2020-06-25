# Simple program to introduce functions
# It receives width and height and returns ground's area


def area(a, b):
    print(f'The area is {a*b}')


print(' -- Ground\'s area --')
width = float(input('Width (m): '))
height = float(input('Height (m): '))

area(width, height)
