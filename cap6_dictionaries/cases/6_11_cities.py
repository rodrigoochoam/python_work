#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the infor- mation you have stored about it.

cities = {
    'dublin': {
        'country': 'ireland',
        'population': '1.5m',
        'fact': 'bar hopping is nice in dublin!',
    },
    'brussels': {
        'country': 'belgium',
        'population': '2.5m',
        'fact': 'gauffres and fries are nice!'
    },
    'london': {
        'country': 'england',
        'population': '14.8m',
        'fact': 'it is very expensive!'
    },
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    print(f"\tCountry: {city_info['country'].title()} ")
    print(f"\tAprox. Population: {city_info['population'].title()} ")
    print(f"\tFact: {city_info['fact'].title()} ")
