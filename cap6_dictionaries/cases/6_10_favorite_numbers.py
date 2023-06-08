#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'rodrigo': [23, 12, 35],
    'álvaro': [8, 9, 10],
    'pablo': [13, 14, 15],
    'papá': [9, 55, 43],
    'mamá': [27, 30, 48],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t-{number}")

