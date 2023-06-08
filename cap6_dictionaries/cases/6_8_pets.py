#6-8. Pets: Make several dictionaries, where each dictionary represents a differ- ent pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pets = []

pet_1 = {
    'Kind': 'Dog',
    'Name': 'Matilda',
    'DOB': '01/11/2022',
    'Owner': 'Rodrigo Ochoa',
}

pets.append(pet_1)

pet_2 = {
    'Kind': 'Dog',
    'Name': 'Manchas',
    'DOB': '17/09/2005',
    'Owner': 'Rodrigo Ochoa',
}

pets.append(pet_2)

pet_3 = {
    'Kind': 'Dog',
    'Name': 'Laika',
    'DOB': '04/06/2012',
    'Owner': 'Rodrigo Ochoa',
}

pets.append(pet_3)

for pet in pets:
    print(f"\nHere's what I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

