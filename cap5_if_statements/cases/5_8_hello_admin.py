#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.

usernames = ['rodrigo', 'carlos', 'antonio', 'admin', 'álvaro']

#If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like yo see a status report?")
    else:  #Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
        print(f"Hello {username.title()}, thank you for logging in again.")



