#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 . Use a for loop to print each number .
numbers = []
for odd_number in range(1,21,2):
    numbers.append(odd_number)
print(numbers)