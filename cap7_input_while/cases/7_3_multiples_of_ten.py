#7-3

number = input("Please give me a number, I will tell you if it is a multiple of ten or not. ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of ten!")
else:
    print(f"{number} is not a multiple of ten :(")


