#7-6-2
#• Use an active variable to control how long the loop runs.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
    else:
        active = False
