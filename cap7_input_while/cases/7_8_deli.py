#7-8

sandwich_orders = ['tuna', 'salmon', 'pollo', 'jamón']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()

    print(f"Making your {finished.title()} sandwich!")
    finished_sandwiches.append((finished))

print("\nThis are the sandwiches that I made for you!")
for sandwich in finished_sandwiches:
    print(sandwich.title())

