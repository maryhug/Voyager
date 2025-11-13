
# SISTEMA DE GESTIÓN DE INVENTARIO



# Lista vacía donde guardaremos todos los productos
inventario = []


# FUNCIÓN 1: AGREGAR PRODUCTO (TASK 2)

def agregar_producto():
    """
    Esta función pide los datos de un producto y lo agrega al inventario.
    Valida que precio y cantidad sean números positivos.
    """
    print("\n--- AGREGAR PRODUCTO ---")
    
    # Pedimos el nombre del producto
    nombre = input("Nombre del producto: ")
    
    # Bucle while para validar el precio (TASK 1 - Validación)
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0:
                print("❌ El precio no puede ser negativo. Intenta de nuevo.")
            else:
                break  # Si es válido, salimos del bucle
        except ValueError:
            print("❌ Por favor ingresa un número válido.")
    
    # Bucle while para validar la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa. Intenta de nuevo.")
            else:
                break
        except ValueError:
            print("❌ Por favor ingresa un número entero válido.")
    
    # Creamos un diccionario con los datos del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregamos el producto a la lista inventario
    inventario.append(producto)
    print(f"✅ Producto '{nombre}' agregado exitosamente.")



# FUNCIÓN 2: MOSTRAR INVENTARIO (TASK 3)

def mostrar_inventario():
    """
    Recorre todos los productos del inventario y los muestra.
    Si está vacío, muestra un mensaje.
    """
    print("\n--- INVENTARIO ACTUAL ---")
    
    # Validamos si hay productos
    if len(inventario) == 0:
        print("📦 El inventario está vacío.")
        return  # Salimos de la función
    
    # Bucle for para recorrer cada producto (TASK 3)
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")



# FUNCIÓN 3: CALCULAR ESTADÍSTICAS (TASK 4)

def calcular_estadisticas():
    """
    Calcula el valor total del inventario y la cantidad total de productos.
    """
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    
    # Validamos si hay productos
    if len(inventario) == 0:
        print(" No hay productos para calcular estadísticas.")
        return
    
    # Variables para acumular totales
    valor_total = 0
    cantidad_total = 0
    
    # Recorremos cada producto para sumar (TASK 4)
    for producto in inventario:
        valor_total += producto['precio'] * producto['cantidad']
        cantidad_total += producto['cantidad']
    
    # Mostramos resultados
    print(f" Valor total del inventario: ${valor_total:.2f}")
    print(f" Cantidad total de productos: {cantidad_total}")
    print(f" Tipos de productos registrados: {len(inventario)}")



# FUNCIÓN 4: MOSTRAR MENÚ (TASK 1)

def mostrar_menu():
    """
    Muestra las opciones disponibles para el usuario.
    """
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("="*40)



# PROGRAMA PRINCIPAL (TASK 2 - Bucle while)

def main():
    """
    Función principal que ejecuta el menú en un bucle.
    """
    print(" ¡Bienvenido al Sistema de Inventario!")
    
    # Bucle infinito hasta que el usuario elija salir (TASK 2)
    while True:
        mostrar_menu()
        
        # Pedimos la opción al usuario
        opcion = input("\nElige una opción (1-4): ")
        
        # Condicionales para procesar la opción (TASK 1)
        if opcion == "1":
            agregar_producto()
        
        elif opcion == "2":
            mostrar_inventario()
        
        elif opcion == "3":
            calcular_estadisticas()
        
        elif opcion == "4":
            print("\n ¡Gracias por usar el sistema! Hasta pronto.")
            break  # Salimos del bucle while
        
        else:
            # Opción inválida (TASK 1 - Validación)
            print(" Opción inválida. Por favor elige entre 1 y 4.")



# EJECUTAR EL PROGRAMA

if __name__ == "__main__":
    main()

