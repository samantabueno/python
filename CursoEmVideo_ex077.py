#Exercise to training tuples
#Program to know the vowals of words inside the tuple

words = ('Manuella', 'Samanta', 'Enir', 'Eli')

for c in words:
    print(f'\nThe vowels of word {c} are: ', end='')
    for x in c:
        if c.lower() in ('aeiou'):
            print(c.lower(), end='')


