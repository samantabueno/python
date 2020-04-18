#Exercice to training repetition structure and string treatment

statment = str(input('Type a statment: ')).strip().lower().replace(' ', '')
palindrome = False
reverse = statment[::-1]

'''
length = len(statment)
for c in range(0, length):
    if statment[c] == statment[length - c - 1]:
        palindrome = True
    else:
        palindrome = False
        break
'''
if statment == reverse:
#if palindrome:
    print('This statment is palindrome!')
else:
    print('This statment is NOT palindrome!')
