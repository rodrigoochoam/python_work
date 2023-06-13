def describe_city(city, country='mexico'):
    """This function tells the country of a city."""
    print(f"{city.title()} is in {country.title()}. ")

describe_city('guadalajara')
describe_city('ciudad de méxico')
describe_city('london', 'england')
