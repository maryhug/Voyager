# Función para agregar nuevos productos al inventario
def agregar_producto():
    # Bucle infinito para validar el nombre del producto
    while True:
        # Solicita el nombre y capitaliza la primera letra
        nombre = input("\nIngrese el nombre del producto: ").capitalize()
        # Validación: nombre no puede estar vacío
        if not nombre:
            print("El nombre no puede estar vacío")
        # Validación: nombre no puede contener solo números
        elif nombre.isdigit():
            print("El nombre no puede contener solo números")
        else:
            print("Nombre registrado correctamente")
            break  # Sale del bucle cuando el nombre es válido
    
    # Bucle infinito para validar el precio del producto
    while True:
        try:
            # Intenta convertir el input a float
            precio = float(input("\nIngrese el precio del producto: $"))
            # Validación: precio debe ser mayor a 0
            if precio <= 0:
                print("El precio no puede ser negativo ni igual a 0")  
            else:
                print("Precio registrado correctamente")
                break  # Sale del bucle cuando el precio es válido
        # Captura error si el input no se puede convertir a float
        except ValueError:
            print("Valor inválido. Ingrese un precio válido para el producto")
    
    # Bucle infinito para validar la cantidad del producto
    while True:
        try:
            # Intenta convertir el input a entero
            cantidad = int(input("\nIngrese la cantidad: "))
            # Validación: cantidad debe ser mayor a 0
            if cantidad <= 0:
                print("La cantidad no puede ser negativa ni igual a 0")  
            else:
                print("Cantidad registrada correctamente")
                break  # Sale del bucle cuando la cantidad es válida
        # Captura error si el input no se puede convertir a int
        except ValueError:
            print("Valor inválido. Ingrese una cantidad válida para el producto")

    # Crea un diccionario con la información del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agrega el producto a la lista global de inventario
    inventario.append(producto)
    
# Función para mostrar todos los productos en el inventario
def mostrar_inventario():
    # Verifica si el inventario está vacío
    if not inventario:
        print("\nEl inventario está vacío.")
    
    else:
        # Imprime el encabezado de la tabla
        print(f"{"Producto":<17} {"Precio":<17} {"Cantidad":<17}")
        i = 1  # Contador para numerar los productos
        # Itera sobre cada producto en el inventario
        for producto in inventario:
            # Imprime cada producto formateado en columnas
            print(f"{i}. {producto["nombre"].capitalize():<15}| ${producto["precio"]:<15}| {producto["cantidad"]:<15}")
            i += 1  # Incrementa el contador

# Función para calcular estadísticas del inventario
def calcular_estadisticas():
        sumatoria = 0  # Acumula el valor total del inventario
        i = 0  # Contador de productos
        # Itera sobre cada producto en el inventario
        for producto in inventario:
            # Calcula el valor total por producto (precio * cantidad)
            pagar_producto = producto["precio"] * producto["cantidad"]
            # Suma al total general
            sumatoria = sumatoria + pagar_producto
            i += 1  # Incrementa el contador de productos
        
        # Retorna ambos valores calculados
        return sumatoria, i

# Lista global que almacena todos los productos
inventario = []
# Variable para controlar la opción del menú
opcion = 0

# Bucle principal del programa - se ejecuta hasta que el usuario elija salir
while opcion != 4:
    
    # Muestra el menú de opciones
    print("\nMenú:")
    print("\n1. Agregar producto")
    print("2. Mostrar Inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    # Solicita la opción al usuario
    opcion = int(input("\n¿Qué desea hacer?: "))
    
    # Opción 1: Agregar producto
    if opcion == 1:
        print("\nAGREGAR PRODUCTO")
        # Bucle para permitir agregar múltiples productos
        while True:
            agregar_producto()  # Llama a la función para agregar producto
            # Pregunta si desea agregar otro producto
            opcion_agg = input("\n¿Desea agregar otro producto? (si/no): ").lower()  
                
            if opcion_agg == 'no':
                break  # Sale del bucle si el usuario no quiere agregar más
    
    # Opción 2: Mostrar inventario
    elif opcion == 2:
        print("\nINVENTARIO")
        mostrar_inventario()  # Llama a la función para mostrar el inventario

    # Opción 3: Calcular estadísticas
    elif opcion == 3:
        print("\nESTADÍSTICAS")
        # Verifica si hay productos en el inventario
        if inventario:
            # Obtiene el valor total y cantidad de productos
            valor_total, i = calcular_estadisticas()
            # Muestra las estadísticas calculadas
            print(f"\nEl valor total del inventario es de: ${valor_total}")
            print(f"En el inventario actualmente hay {i} productos") 
        else:
            print("\nEL inventario está vacío")
    
    # Opción 4: Salir del programa
    elif opcion == 4:
        print("Saliendo del programa...")

    # Opción inválida: número fuera del rango del menú
    else:
        print("\nValor inválido. Ingrese un número dentro del rango.")