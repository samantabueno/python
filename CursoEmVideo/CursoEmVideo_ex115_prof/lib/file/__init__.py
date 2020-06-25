from CursoEmVideo.CursoEmVideo_ex115_prof.lib.interface import title


def create(name_file):
    try:
        a = open(name_file, 'a') #create if not exists
        a.close()
    except:
        print('File error!')


def read(name_file):
    title('REGISTERED PEOPLE')
    try:
        a = open(name_file, 'r')
        for person in a:
            print(f'{person.split(";")[0]:<37}{person.split(";")[1]:>3}', end='')

    except:
        print('Read File error!')


def save(name_file, name='unknown', age=0):
    try:
        a = open(name_file, 'at')
        a.write(f'{name};{age}\n')
    except:
        print('File write error!')
    else:
        print(f'{name} added with success!')

