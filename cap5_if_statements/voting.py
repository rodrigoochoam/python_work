age = int(input("Please enter your age: "))

if age >= 18:
    print("You are old enough to vote!")
    registered = input("Have you registered to vote? (YES/NO)").upper()
    if registered == 'YES':
        print("Nice")
    else:
        print("Please register to vote!!")
else:
    print("Sorry, you are not old enough to vote yet.")
    print("Please register to vote as soon as you turn 18!")
