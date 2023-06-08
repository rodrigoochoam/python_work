#3-6. More Guests: You just found a bigger dinner table, so now more space is available . Think of three more guests to invite to dinner .

#Start with your program from Exercise 3-5 . 
guest_list = ['mamá', 'papá', 'álvaro', 'pablo']
message = ", me gustaría que vinieras a cenar conmigo!"

print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)

print("\n------------------------------------------")

print("Pablo no vendrá con nosotros, él tiene clase :(")

guest_list[3] = 'tita'

print("\n------------------------------------------")

print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)

print("\n------------------------------------------")

#Add a print statement to the end of your program informing people that you found a bigger dinner table .
message_2 = ", reservé una mesa más grande, ¡para que vengan más personas!"
print(guest_list[0].title() + message_2)
print(guest_list[1].title() + message_2)
print(guest_list[2].title() + message_2)
print(guest_list[3].title() + message_2)

#Use insert() to add one new guest to the beginning of your list..
guest_list.insert(0, 'tito')

#Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'karen')

#Use append() to add one new guest to the end of your list .
guest_list.append('sofi')

#Espacio
print("\n------------------------------------------")

#Print a new set of invitation messages, one for each person in your list .
print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)
print(guest_list[4].title() + message)
print(guest_list[5].title() + message)
print(guest_list[6].title() + message)
print(guest_list)