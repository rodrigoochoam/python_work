#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations . You’ll have to think of someone else to invite .

#Start with your program from Exercise 3-4 . 
guest_list = ['mamá', 'papá', 'álvaro', 'pablo']
message = ", me gustaría que vinieras a cenar conmigo!"

print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)

#Espacio
print("\n------------------------------------------")

#Add a print statement at the end of your program stating the name of the guest who can’t make it .
print("Pablo no vendrá con nosotros, él tiene clase :(")

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting .
guest_list[3] = 'Tita'

#Espacio
print("\n------------------------------------------")

#Print a second set of invitation messages, one for each person who is still in your list .
print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)