# Carrito de compras.

# Lista global que almacena los productos del carrito
carrito = []

# Muestra el menú principal con las opciones disponibles.
# No recibe parámetros ni retorna valores.
def mostrar_menu():
    print("\n=== Carrito de Compras ===")
    print("1) Agregar producto")
    print("2) Ver carrito")
    print("3) Eliminar producto")
    print("4) Total y pagar")
    print("5) Salir")

# Solicita y valida un precio numérico al usuario.
def pedir_precio(mensaje):
    entrada = input(mensaje).replace(',', '.').strip()
    # Bucle de validación: continúa hasta recibir un número válido
    while not (entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1):
        entrada = input("Precio inválido. Ingresa un número (ej: 12.50): ").replace(',', '.').strip()
    return float(entrada)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()
    # Opción 1: Agregar producto al carrito
    if opcion == "1":
        # Solicitar nombre del producto
        nombre = input("Nombre del producto: ").strip()
        # Validación nombre no sea un campo vacío
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()
        # Solicitar precio usando la función de validación
        precio = pedir_precio("Precio: ")
        # Agregar producto al carrito como diccionario
        carrito.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' agregado.")

    # Opción 2: Ver todos los productos en el carrito
    elif opcion == "2":
        if not carrito:
            print("El carrito está vacío.")
        else:
            print("\nCarrito:")
            # enumerate(cart, 1) Genera índices comenzando desde 1
            for i, item in enumerate(carrito, 1):
                # Formato del precio con 2 decimales
                print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")

    # Opción 3: Eliminar un producto del carrito
    elif opcion == "3":
        if not carrito:
            print("No hay productos para eliminar.")
        else:
            # Mostrar lista numerada de productos
            for i, item in enumerate(carrito, 1):
                print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")
            # Solicitar índice del producto a eliminar
            index = input("Número del producto a eliminar (o Enter para cancelar): ").strip()
            if index.isdigit():
                index = int(index)
                # Verificar que el índice esté dentro del rango válido
                if 1 <= index <= len(carrito):
                    # pop(idx-1) elimina y retorna el elemento en la posición idx-1
                    eliminado = carrito.pop(index - 1)
                    print(f"Eliminado: {eliminado['nombre']}")
                else:
                    print("Índice fuera de rango.")
            else:
                # Si no ingresó un número, cancelar la operación
                print("Eliminación cancelada.")

    # Opción 4: Calcular total y procesar pago
    elif opcion == "4":
        if not carrito:
            print("Carrito vacío.")
        else:
            # Calcular subtotal sumando los precios de todos los productos
            subtotal = sum(item['precio'] for item in carrito)
            print(f"Subtotal: ${subtotal:.2f}")
            # Solicitar código de descuento (opcional)
            descuento = input("¿Tienes código de descuento? Ingresa porcentaje (ej: 10) o deja vacío: ").replace(',', '.').strip()
            if descuento == "":
                # Sin descuento, el total es igual al subtotal
                total = subtotal
            else:
                # Validar que el descuento sea un número
                if descuento.replace('.', '', 1).isdigit():
                    d = float(descuento)
                    # Verificar que el descuento esté entre 0 y 100%
                    if 0 <= d <= 100:
                        # Aplicar descuento: total = subtotal × (1 - descuento/100)
                        total = subtotal * (1 - d/100)
                    else:
                        print("Descuento inválido, se ignorará.")
                        total = subtotal
                else:
                    print("Descuento inválido, se ignorará.")
                    total = subtotal
            print(f"Total a pagar: ${total:.2f}")

            # Confirmar pago y vaciar carrito
            confirmar = input("Confirmar pago y vaciar carrito? (s/n): ").strip().lower()
            if confirmar == "s":
                # clear() elimina todos los elementos de la lista
                carrito.clear()
                print("Pago realizado. Carrito vacío.")
            else:
                print("Pago cancelado.")

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Saliendo del carrito. ¡Hasta luego!")
        break   # Rompe el bucle while y termina el programa
    # Opción inválida del menú
    else:
        print("Opción inválida.")
