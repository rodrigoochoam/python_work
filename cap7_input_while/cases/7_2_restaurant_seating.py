#7-2.
dinner_group = input("A table for how many? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("You will have to wait a little.")
else:
    print("Your table is ready!")