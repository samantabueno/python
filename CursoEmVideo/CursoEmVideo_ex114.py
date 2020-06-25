def try_site(url):
    import requests
    try:
        a = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Error. Please, enter "http://"')
    except requests.exceptions.ConnectionError:
        print('Unavailable Site. Verify your connection.')
    except Exception as err:
        print('Unknown error.', err.__class__)
    else:
        print('Available site.')


# Main Program
try_site('http://www.pudim.com.br')
