countries = {
    'mexico' : 122,
    'colombia' : 49,
    'argentina' : 43,
    'chile': 18,
    'peru': 31
}

if __name__ == '__main__':
    country = input('Type a country name: ').lower()
    try:
        print('La poblacion de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato del pais {}'.format(country))