my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
