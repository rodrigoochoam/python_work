print("**BIENVENIDO A RESTAURANT NICKSANE**")
print("Este es el sistema de cobranza de NICKSANE")
print("- Esta es tu tarjeta de prepago. Te hemos abonado $1,000.00 pesos para iniciar.")
print("- Es necesario que definas una clave de acceso para poder comenzar.")
print("* Sólo se autorizan dígitos numéricos. *")
password = int(input())
print("Por favor confirma tu contraseña ingresada: ")
clave = int(input())

if clave == password:
    print("Acceso concedido")
    print("Selecciona la opción que desees realizar:")
    
    acumma = 0
    acummn = 0
    
    while True:
        print("\t +++ MENÚ NICKSANE+++")
        print("\t++++++++++++++++++++++\n")
        print("\t 1. Comida para adultos")
        print("\t 2. Menú de niños")
        print("\t 3. Realizar pago")
        print("\t 4. Recarga Tarjeta de Prepago")
        print("\t 5. S A L I R")
        print("\t++++++++++++++++++++++\n")
        menu = int(input())
        
        if menu == 1:
            print("--- Menú Platillos para Adultos ---")
            print("1. Langosta, champagne y papas al ajo. Precio: $800")
            print("2. Rib-Eye, vino tinto y ensalada. Precio: $600")
            print("3. Salmón, vino blanco y espinacas a la crema. Precio: $500")
            menuadultos = int(input())
            
            if menuadultos == 1:
                print("-- Langosta, champagne y papas al ajo. Precio: $800 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalma = cuantas * 800
                acumma += totalma
                
            elif menuadultos == 2:
                print("-- Rib-Eye, vino tinto y ensalada. Precio: $600 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalma = cuantas * 600
                acumma += totalma
                
            elif menuadultos == 3:
                print("-- Salmón, vino blanco y espinacas a la crema. Precio: $500 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalma = cuantas * 500
                acumma += totalma
                
        elif menu == 2:
            print("--- Menú Platillos para Niños ---")
            print("1. Hamburguesa, refresco, papas a la francesa y nieve de vainilla. Precio: $300")
            print("2. Nuggets, refresco, flan. Precio: $200")
            print("3. Hot-dogs, papas a la francesa y refresco. Precio: $250")
            menuniños = int(input())
            
            if menuniños == 1:
                print("-- Hamburguesa, refresco, papas a la francesa y nieve de vainilla. Precio: $300 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalmn = cuantas * 300
                acummn += totalmn
                
            elif menuniños == 2:
                print("-- Nuggets, refresco, flan. Precio: $200 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalmn = cuantas * 200
                acummn += totalmn
                
            elif menuniños == 3:
                print("-- Hot-dogs, papas a la francesa y refresco. Precio: $250 --")
                print("¿Cuántas deseas adquirir?")
                cuantas = float(input())
                totalmn = cuantas * 250
                acummn += totalmn
                
        elif menu == 3:
            print("--- Realizar pago ---")
            total = acumma + acummn
            print(f"El total a pagar es: ${total:.2f}")
            print("Ingresa la cantidad a pagar:")
            pago = float(input())
            
            if pago >= total:
                cambio = pago - total
                print(f"Cambio: ${cambio:.2f}")
                print("Gracias por tu compra. ¡Vuelve pronto!")
                break
            else:
                print("La cantidad ingresada no es suficiente. Por favor, ingresa un monto válido.")
                
        elif menu == 4:
            print("--- Recarga Tarjeta de Prepago ---")
            print("Ingresa la cantidad a recargar:")
            recarga = float(input())
            
            if recarga > 0:
                acumma = 0
                acummn = 0
                print(f"Se ha recargado ${recarga:.2f} a tu tarjeta de prepago.")
                print("¡Disfruta de tu comida!")
            else:
                print("La cantidad ingresada no es válida. Por favor, ingresa un monto mayor a 0.")
                
        elif menu == 5:
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            
else:
    print("Acceso denegado")
