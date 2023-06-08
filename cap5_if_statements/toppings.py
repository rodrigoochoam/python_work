available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = []

for i in range(3):
    topping = input(f"Enter topping {i+1}: ")
    requested_toppings.append(topping)

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#In this code, the range(3) function is used to loop three times and ask for input. The user's input is then appended to the requested_toppings list using the append() method. Finally, the code loops through the requested_toppings list and checks if each topping is in the available_toppings list, printing a message accordingly.