# Inicializar lista vacía para almacenar el inventario
lista = []

# Iniciar ciclo infinito para mantener el programa ejecutándose
while True:
    # Mostrar menú de opciones al usuario
    print("\nMenu Inventario")
    print("1. Ingresar producto")
    print("2. Sacar costo total del producto")
    print("3. Listar producto")
    print("4. Salir")

    # Solicitar opción del menú con manejo de errores
    opcion = int(input("¿Qué opción desea realizar? "))

    # Opción 1: Ingresar productos al inventario
    if opcion == 1:
        # Solicitar cantidad de productos a ingresar
        try:
            datos = int(input("¿Cuántos productos deseas ingresar al inventario? "))
        except ValueError:
            print("Debes ingresar un número entero.")
            continue

        # Validar que la cantidad sea mayor a 0
        while datos <= 0:
            print("El número de productos a ingresar no puede ser igual o menor a 0.")
            try:
                datos = int(input("¿Cuántos productos deseas ingresar al inventario? "))
            except ValueError:
                print("Debes ingresar un número entero.")
                datos = 0

        # Iterar para ingresar cada producto
        for i in range(datos):
            # Validación para nombre del producto
            while True:
                # Solicitar nombre del producto
                producto = input(f"\nIngresa el nombre del producto #{i + 1}: ").strip()
                if producto == "":
                    print("El nombre no puede estar vacío ni contener solo espacios. Intenta de nuevo.")
                    continue
                break

            # Solicitar y validar precio del producto
            while True:
                try:
                    precio = float(input("Ingresa el precio por unidad del producto: "))
                    if precio <= 0:
                        print("El precio no puede ser negativo ni cero. Intenta de nuevo.")
                        continue
                    break

                except ValueError:
                    print("Precio inválido. Ingresa un número (p. ej. 1500.0).")

            # Solicitar y validar cantidad del producto
            while True:
                try:
                    cantidad = int(input("Ingresa la cantidad de productos: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor que 0. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Cantidad inválida. Ingresa un número entero.")

            # Buscar si el producto ya existe en el inventario
            encontrado = False
            for item in lista:
                if item['producto'].lower() == producto.lower():
                    # Si existe, actualizar cantidad y precio
                    item['cantidad'] += cantidad
                    item['precio'] = precio
                    encontrado = True
                    break

            # Si no existe, agregar nuevo producto al inventario
            if not encontrado:
                lista.append({"producto": producto, "precio": precio, "cantidad": cantidad})

        # Preguntar si desea ver los productos ingresados
        decision = input("\n¿Desea ver los productos ingresados? (S/N) ").strip().lower()
        if decision == "s":
            # Mostrar inventario actual si hay productos
            if lista:
                print("\nInventario actual:")
                for item in lista:
                    print(f"- Producto: {item['producto']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
            else:
                print("El inventario está vacío.")
        else:
            continue

    # Opción 2: Calcular costo total de un producto específico
    elif opcion == 2:
        # Verificar que el inventario no esté vacío
        if not lista:
            print("\nEl inventario está vacío. Ingresa productos primero.")
            continue

        # Solicitar nombre del producto a buscar
        buscar_producto = input("\nProducto al que le desea sacar el costo total: ").strip()
        encontrado = False

        # Buscar el producto en el inventario
        for item in lista:
            if item.get('producto', '').lower() == buscar_producto.lower():
                # Calcular y mostrar costo total del producto
                costo_total = item["precio"] * item["cantidad"]
                print(
                    f"- Producto: {item['producto']} | Precio: {item['precio']} | Cantidad: {item['cantidad']} | Total: {costo_total:.3f}")
                encontrado = True
                break

        # Informar si el producto no fue encontrado
        if not encontrado:
            print("El producto no existe en el inventario.")

    # Opción 3: Listar todos los productos del inventario
    elif opcion == 3:
        print("\nInventario actual:")
        # Mostrar cada producto con sus detalles
        if lista:
            for item in lista:
                print(f"- Producto: {item['producto']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
        else:
            print("El inventario está vacío.")
    # Opción 4: Salir del programa
    elif opcion == 4:
        print("¡Hasta luego!")
        break

    # Manejar opciones no válidas
    else:
        print("Opción no válida, intente de nuevo.")

# Este es un sistema de gestión de inventario desarrollado en Python que permite
# administrar productos mediante un menú interactivo de 4 opciones:

# Funcionalidad principal:
# El programa mantiene un inventario de productos en memoria (lista de diccionarios)
# donde cada producto tiene nombre, precio unitario y cantidad. Opera en un ciclo continuo
# hasta que el usuario decide salir.

# Opciones disponibles:
# 1. Ingresar producto: Permite agregar uno o varios productos al inventario. Si el producto ya
# existe, actualiza su cantidad (sumándola) y precio. Incluye validaciones robustas para asegurar
# que precios y cantidades sean valores positivos válidos.

# 2. Calcular costo total: Busca un producto específico por nombre y calcula su valor total multiplicando
# precio × cantidad, mostrando toda la información del producto.

# 3. Listar productos: Muestra el inventario completo con todos los productos y sus detalles
# (nombre, precio, cantidad).

# 4. Salir: Termina la ejecución del programa.