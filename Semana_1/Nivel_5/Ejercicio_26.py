# Carrito de compras.

cart = []

def mostrar_menu():
    print("\n=== Carrito de Compras ===")
    print("1) Agregar producto")
    print("2) Ver carrito")
    print("3) Eliminar producto")
    print("4) Total y pagar")
    print("5) Salir")

def pedir_precio(mensaje):
    entrada = input(mensaje).replace(',', '.').strip()
    while not (entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1):
        entrada = input("Precio inválido. Ingresa un número (ej: 12.50): ").replace(',', '.').strip()
    return float(entrada)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()
        precio = pedir_precio("Precio: ")
        cart.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' agregado.")
    elif opcion == "2":
        if not cart:
            print("El carrito está vacío.")
        else:
            print("\nCarrito:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")
    elif opcion == "3":
        if not cart:
            print("No hay productos para eliminar.")
        else:
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")
            idx = input("Número del producto a eliminar (o Enter para cancelar): ").strip()
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(cart):
                    eliminado = cart.pop(idx-1)
                    print(f"Eliminado: {eliminado['nombre']}")
                else:
                    print("Índice fuera de rango.")
            else:
                print("Eliminación cancelada.")
    elif opcion == "4":
        if not cart:
            print("Carrito vacío.")
        else:
            subtotal = sum(item['precio'] for item in cart)
            print(f"Subtotal: ${subtotal:.2f}")
            desc = input("¿Tienes código de descuento? Ingresa porcentaje (ej: 10) o deja vacío: ").replace(',', '.').strip()
            if desc == "":
                total = subtotal
            else:
                if desc.replace('.', '', 1).isdigit():
                    d = float(desc)
                    if 0 <= d <= 100:
                        total = subtotal * (1 - d/100)
                    else:
                        print("Descuento inválido, se ignorará.")
                        total = subtotal
                else:
                    print("Descuento inválido, se ignorará.")
                    total = subtotal
            print(f"Total a pagar: ${total:.2f}")
            # Vaciar carrito después de "pago"
            confirmar = input("Confirmar pago y vaciar carrito? (s/n): ").strip().lower()
            if confirmar == "s":
                cart.clear()
                print("Pago realizado. Carrito vacío.")
            else:
                print("Pago cancelado.")
    elif opcion == "5":
        print("Saliendo del carrito. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
