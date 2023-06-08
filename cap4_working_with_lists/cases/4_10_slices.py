#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

friends_names = ['sebastián', 'andrés', 'alfredo', 'josé david', 'diegon']

#Print the message, The first three items in the list are: . Then use a slice to print the first three items from that program’s list .
print("The first three items in the list are:")
for friend in friends_names[0:3]:
    print(friend.title())

#Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle of the list .
print("\nThree items from the mmiddle of the list are:")
for friend in friends_names[1:4]:
    print(friend.title())

#Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .
print("\nThe last three items in the list are:")
for friend in friends_names[-3:]:
    print(friend.title())