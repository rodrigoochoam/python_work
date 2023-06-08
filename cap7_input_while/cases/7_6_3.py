#7-6_3
#• Use a break statement to exit the loop when the user enters a 'quit' value.


prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        break
