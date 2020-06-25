# Exercise to training tuples
# Program that returns the vowels of some words inside the tuple

words = ('Manuella', 'Samanta', 'Enir', 'Eli')

for c in words:
    print(f'\nThe vowels of word {c} are: ', end='')
    for x in c:
        if c.lower() in ('aeiou'):
            print(c.lower(), end='')


