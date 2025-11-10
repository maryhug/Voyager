# Solicitar datos al usuario
# Iniciar un bucle hasta que ingrese el tipo de dato correcto
while True:
    nombre = (input("Ingrese el nombre del producto: "))
# Verificar que el nombre sea registrado correctamente
    if not nombre:
        print("El nombre no puede estar vacío.")
    elif nombre.startswith('-'):
        print("El nombre no puede comenzar por un signo negativo")
    elif nombre.isdigit():
        print("El nombre no puede contener solo números.")
    else:
        print("Nombre registrado correctamente.")
        break

# Iniciar un bucle hasta que ingrese el tipo de dato correcto
while True:

# Verificar que el precio sea tipo flotante
    try:
        precio = float(input("Ingrese el precio del producto: $"))
        if precio <= 0:
            print("El precio no puede ser negativo ni igual a 0")
        else:
            print("Precio registrado correctamente.")
            break
    except ValueError:
        print("Valor inválido. Ingrese un precio válido para el producto.")

# Iniciar un bucle hasta que ingrese el tipo de dato correcto
while True:

# Con los comandos "try - except" verificar que la cantidad sea tipo entero
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <= 0:
            print("La cantidad no puede ser negativa ni igual a 0")
        else:
            print("Cantidad registrada correctamente.")    
            break
    except ValueError:
        print("Valor inválido. Ingrese una cantidad válido para el producto.")

# Calcular el costo total con los datos ingresados del precio y la cantidad
costo_total = precio * cantidad

# Mostrar el resultado en consola
print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad} | Total: ${costo_total}")