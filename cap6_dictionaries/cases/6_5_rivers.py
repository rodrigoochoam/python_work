#6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {
    'nile': 'egypt',
    'bravo': 'us-mex',
    'danubio': 'hungary',
    }

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print(f"The {river.title()} runs thorugh {country.title()}.")

#Use a loop to print the name of each river included in the dictionary.
for river in rivers.keys():
    print(river.title())

#Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(country.title())
    