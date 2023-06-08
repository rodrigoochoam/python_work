#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests .

#Start with your program from Exercise 3-6 . 
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

#Espacio
print("\n------------------------------------------")

#Add a new line that prints a message saying that you can invite only two people for dinner .
message_3 = ", lo siento, sólo podré invitar a 2 personas a la cena... Me quedé sin dinero."
print(guest_list[0].title() + message_3)
print(guest_list[1].title() + message_3)
print(guest_list[2].title() + message_3)
print(guest_list[3].title() + message_3)
print(guest_list[4].title() + message_3)
print(guest_list[5].title() + message_3)
print(guest_list[6].title() + message_3)

#Espacio
print("\n------------------------------------------")

#Use pop() to remove guests from your list one at a time until only two names remain in your list . Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner .
eliminado_1 = guest_list.pop(0)
print(eliminado_1.title() + ", lo siento, fuiste eliminado :(")
print(guest_list)
eliminado_2 = guest_list.pop(1)
print(eliminado_2.title() + ", lo siento, fuiste eliminado :(")
print(guest_list)
eliminado_3 = guest_list.pop(2)
print(eliminado_3.title() + ", lo siento, fuiste eliminado :(")
print(guest_list)
eliminado_4 = guest_list.pop(3)
print(eliminado_4.title() + ", lo siento, fuiste eliminado :(")
print(guest_list)
eliminado_5 = guest_list.pop(2)
print(eliminado_5.title() + ", lo siento, fuiste eliminado :(")
print(guest_list)

#Espacio
print("\n------------------------------------------")

#Print a message to each of the two people still on your list, letting them know they’re still invited .
print(guest_list[0].title() + ", sigues invitado, nos vemos a las 08.00h")
print(guest_list[1].title() + ", sigues invitado, nos vemos a las 08.00h")

#Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure you actually have an empty list at the end of your program .
del guest_list[0]
del guest_list[0]

print(guest_list)