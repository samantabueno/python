#Exercise to training tuples.
#Program to transform numbers in numbers in full

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
          'eighteen', 'nineteen', 'twenty')

while True:
    n = int(input('Type a number to know how to write them: '))
    if n in range(0, 21):
        break

print(f'Your number is: {numbers[n]}')


