def title_personalized(title, color=44, manual=False):
    from time import sleep
    len_ = len(title) + 4
    print(f'\033[{color}m-'*len_)
    print(f'  {title}')
    print('-'*len_)
    print('\033[m')
    sleep(0.5)


def help_personalized(name):
    title_personalized(f'Accessing {name} manual', 45)
    help(name)


# Main Program
while True:
    title_personalized('HELP PERSONALISED BY SAMYS')
    n = input('Type the function name that you need help: ')
    if n.upper() == 'X':
        title_personalized('LOG OFF', 47)
        break;
    else:
        help_personalized(n)
