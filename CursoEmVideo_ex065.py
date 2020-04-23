#Exercise to training repetition structure (while)
#Program to show the middle, biggest and least number of N numbers that user typed

cont = 'S'
sum = count = biggest = least = 0

while cont != 'N':
    n = int(input('Type a number: '))
    sum += n
    count = count + 1
    if count == 1:
        least = biggest = n
    else:
        if n < least:
            least = n
        if n > biggest:
            biggest = n
    cont = str(input('Do you want to continue? [S][N]: ')).upper()
    while cont not in ('S', 'N'):
        print('Invalid Option')
        cont = str(input('Do you want to continue? [S][N]: ')).upper()

print('The middle number is: ', sum / count)
print('The biggest number is: ', biggest)
print('The least number is: ', least)
