from CursoEmVideo.CursoEmVideo_ex115_prof.lib.interface import *
from CursoEmVideo.CursoEmVideo_ex115_prof.lib.file import *
from time import sleep

file = 'peopleprof.txt'
create(file)

while True:
    n = menu(['To list registered people', 'To register a person', 'To exit'])
    if n == 1:
        read(file)
    elif n == 2:
        title('NEW REGISTRATION')
        name = input('Name: ')
        age = readInt('Age: ')
        save(file, name, age)
    elif n == 3:
        title('SHUTTING DOWN...')
        break
    else:
        print('Invalid Option =(')
    sleep(2)



