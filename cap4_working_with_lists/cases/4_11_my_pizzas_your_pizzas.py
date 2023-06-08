#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) . Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following:
pizzas = ['pepperoni', 'champiñones', 'queso', 'jamón']
friend_pizzas = pizzas[:] # Make a copy of the list of pizzas, and call it friend_pizzas .

pizzas.append('hawaiana')  #Add a new pizza to the original list .
friend_pizzas.append('tres quesos') #Add a different pizza to the list friend_pizzas .

#Prove that you have two separate lists . Print the message, My favorite pizzas are:, and then use a for loop to print the first list . Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the sec- ond list . Make sure each new pizza is stored in the appropriate list .

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())


