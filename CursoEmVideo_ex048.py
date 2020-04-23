#Exercise to training repetition structure
#Program to know the sum of the numbers odd and multiple of three

sum = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        sum = sum + c
        #print(c, 'is divisible by 3')
print(sum)