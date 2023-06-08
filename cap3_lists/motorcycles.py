motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#Guardamos el valor en una variable
too_expensive = 'ducati'
#Usamos esta variable para decirle a Python qué valor va a remover de la lista
motorcycles.remove(too_expensive)
print(motorcycles)
#the value 'ducati' has been removed from the list but is still stored in the variable too_expensive, allowing us to print a statement about why we removed 'ducati' from the list of motorcycles:
print("\nA " + too_expensive.title() + " is too expensive for me")