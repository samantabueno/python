#Exercice to training repetition structure
#Program to sum the even numbers of six numbers user typed

sum = 0
for c in range(0, 6):
    n = int(input('Type a number ({} de 6): '.format(c+1)))
    if n % 2 == 0:
        sum += n
print(sum)