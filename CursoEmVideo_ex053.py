# Exercise to training repetition structure and string treatment
# Program that receives a word and verify weather it's a palindrome word.
# (Palindrome = same name if you read normal and read back forward like "madam, level, refer")

statement = str(input('Type a statement: ')).strip().lower().replace(' ', '')
palindrome = False
reverse = statement[::-1]

'''
length = len(statement)
for c in range(0, length):
    if statement[c] == statement[length - c - 1]:
        palindrome = True
    else:
        palindrome = False
        break
'''
if statement == reverse:
#if palindrome:
    print('This statement is palindrome!')
else:
    print('This statement is NOT palindrome!')
