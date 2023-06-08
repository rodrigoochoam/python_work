#7-9

sandwich_orders = ['tuna','pastrami', 'salmon', 'pastrami', 'pollo', 'jamón']
finished_sandwiches = []

print("\nThe deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n-------------")

while sandwich_orders:
    finished = sandwich_orders.pop()

    print(f"Making your {finished.title()} sandwich!")
    finished_sandwiches.append((finished))


print("\nThis are the sandwiches that I made for you!")
for sandwich in finished_sandwiches:
    print(sandwich.title())


