#7-6_1
# Use a conditional test in the while statement to stop the loop.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

topping = ''
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
