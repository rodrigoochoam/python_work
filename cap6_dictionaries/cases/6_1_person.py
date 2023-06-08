#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

info_rodrigo = {
    'first_name': 'rodrigo',
    'last_name': 'ochoa',
    'age': 23,
    'city': 'guadalajara',
    }

info_rodrigo_first_name = info_rodrigo['first_name'].title()
info_rodrigo_last_name = info_rodrigo['last_name'].title()
info_rodrigo_age = info_rodrigo['age']
info_rodrigo_city = info_rodrigo['city'].title()

print(f"The information of: {info_rodrigo_first_name} {info_rodrigo_last_name}")
print(f"Age: {info_rodrigo_age}")
print(f"City: {info_rodrigo_city}")
