#Exercise to training tuples.
#Program to transform numbers in numbers in full

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
          'eighteen', 'nineteen', 'twenty')

while True:
    n = int(input('Type a number between 0 and 20 to know how to write them: '))
    if n in range(0, 21):
        break

print(f'Your number is: {numbers[n]}')


