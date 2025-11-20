
# Función para agregar nuevos productos al inventario
def registrar_producto(inventario):

    nombre = validaciones("Ingrese el nombre del producto: ", "str")
        
    precio = validaciones("Ingrese el precio del producto: ", "float")
   
    cantidad = validaciones("\nIngrese la cantidad: ", "int")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)

# Función para editar algún producto del inventario
def editar_producto(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")

# Función para eliminar algún producto del inventario
def eliminar_producto(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
    
# Función para mostrar el inventario
def mostrar_inventario(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
    
#Función para validar el tipo de dato
def validaciones(mensaje, tipo):
    dato = input(mensaje)
    if tipo == "str":
        while not dato.isalpha() or dato == "":
            print("Error: Ingrese un valor válido (solo letras).")
            dato = input(mensaje)
        return dato.capitalize()
    elif tipo == "int":
        while True:
            try:
                numero = int(dato)
                if numero < 0:
                    print("Error: Ingrese un número entero positivo.")
                    dato = input(mensaje)
                    continue
                return numero
            except ValueError:
                print("Error: Ingrese un número entero válido.")
                dato = input(mensaje)
    elif tipo == "float":           
        while True:
            try:
                numero = float(dato)
                if numero < 0:
                    print("Error: Ingrese un número decimal positivo.")
                    dato = input(mensaje)
                    continue
                return numero
            except ValueError:
                print("Error: Ingrese un número decimal válido.")
                dato = input(mensaje)
        
        
        



"""
def agregar_producto(inventario):
    
    nombre = validar_dato(
        "\nIngrese el nombre del producto: ",
        tipo="str",
        no_vacio=True
    )
    print("Nombre registrado correctamente")

    precio = validar_dato(
        "\nIngrese el precio del producto: $",
        tipo="float",
        minimo=0.01    # mayor que 0
    )
    print("Precio registrado correctamente")

    cantidad = validar_dato(
        "\nIngrese la cantidad: ",
        tipo="int",
        minimo=1       # mayor que 0
    )
    print("Cantidad registrada correctamente")

    # Crear producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("\nProducto agregado correctamente.")
"""