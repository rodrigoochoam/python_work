#6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionar- ies in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = {
    'rochoa': {
        'first_name': 'rodrigo',
        'last_name': 'ochoa',
        'age': 23,
        'city': 'guadalajara',
    },

    'pochoa': {
        'first_name': 'pablo',
        'last_name': 'ochoa',
        'age': 22,
        'city': 'guadalajara',    
    },

    'aochoa': {
        'first_name': 'álvaro',
        'last_name': 'ochoa',
        'age': 23,
        'city': 'guadalajara',    
    },
   
}

for person, person_info in people.items():
    print(f"\nUsername: {person}")
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    print(f"\tName: {full_name.title()}")
    print(f"\tAge: {person_info['age']}")
    print(f"\tCity: {person_info['city'].title()}")


    
