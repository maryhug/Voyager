# 24 Carrito de compras 

carrito = {}  # Diccionario para guardar los productos y sus precios

while True:
    print("Bienvenido a compras.com mi compaaa.")
    print("1. Agregar producto.")
    print("2. Eliminar producto.")
    print("3. Ver carrito.")
    print("4. Ver total a pagar.")
    print("5. Salir.")
    
    try:
        opcion = int(input("¿Qué deseas hacer mi compaaa? "))
        
        if opcion == 1:
            # Agrega un producto con su precio
            producto = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            carrito[producto] = precio
            print(f"Se agregó {producto} con precio ${precio}.")
            
        elif opcion == 2:
            # Elimina un producto del carrito
            producto = input("¿Qué producto deseas eliminar? ")
            if producto in carrito:
                del carrito[producto]
                print(f"Se eliminó {producto} del carrito.")
            else:
                print("Ese producto no está mi compaaa.")
                
        elif opcion == 3:
            # Muestra el contenido del carrito
            if not carrito:
                print("El carrito está vacío mi compaaa.")
            else:
                print("Carrito actual:")
                for p, precio in carrito.items():
                    print(f"- {p}: ${precio}")
                    
        elif opcion == 4:
            # Calcula el total a pagar
            total = sum(carrito.values())
            print(f"El total a pagar es ${total}.")
            
        elif opcion == 5:
            # Termina el programa
            print("Gracias por comprar mi compaaa. Dios te bendiga.")
            break
        
        else:
            print("Esa opción no existe mi compaaa.")
            
    except ValueError:
        print("Eso no es un número mi compaaa.")