squares = [] #start with an empty list
for value in range(1,11): #we tell Python to loop through each value from 1 to 10 using the range() function.
    square = value**2 #Inside the loop, the current value is raised to the second power and stored in the variable square
    squares.append(square) #each new value of square is appended to the list squares. 

print(squares)