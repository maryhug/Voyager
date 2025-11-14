# Creación lista para guardar productos del inventario
inventory = []

# Función para ingresar el nombre del producto
def get_product_name():
    while True:
        product = input("Ingrese nombre del producto: ").strip().capitalize()
        # Validación que el nombre no puede estar vació
        if product == "":
            print("Error: El nombre del producto no puede estar vacío.")
            continue
        # Retorna el nombre del producto si todo salio bien
        return product

# Función para ingresar el precio del producto
def get_price():
    while True:
        raw = input("Ingrese precio del producto: ").strip()
        # Validación que el precio no puede estar vació
        if raw == "":
            print("Error: El precio del producto no puede estar vacío.")
            # Vuelve a preguntar el raw, las veces que sea necesaria hasta que el usuario ingrese un precio correcto
            continue
        # Manejo de errores
        try:
            # Convierte el precio ingresado por el usuario en float y la guarda en una variable
            price = float(raw)
            # Si el precio ingresado es negativo o 0, saca error y vuelve a pedir el precio
            if price <= 0:
                print(f"Error: {price} No puede ser negativo o 0.")
                continue
            return price
        except ValueError:
            # Si el precio es no entra en un float vuelve a pedir el precio
            print("Error: El precio debe ser un número válido.")

# Función para ingresar la cantidad del producto
def get_quantity():
    while True:
        raw = input("Ingrese la cantidad de productos: ").strip()
        # Validación que la cantidad no puede estar vacía
        if raw == "":
            print("Error: La cantidad del producto no puede estar vacío.")
            continue
        try:
            # Convierte la cantidad ingresada por el usuario en int y la guarda en una variable
            quantity = int(raw)
            # Si la cantidad ingresada es negativo o 0, saca error y vuelve a pedir la cantidad
            if quantity <= 0:
                print(f"Error: {quantity} No puede ser negativo o 0.")
                continue
            return quantity
        except ValueError:
            # Si la cantidad no es entera vuelve a pedir el precio
            print("La cantidad debe ser entera")

# Función para modificar el precio y la cantidad si el producto existe y el usuario desea modificarla
def handle_existing_product(product):
    # Busca el primer diccionario en `inventory` cuyo campo "Producto" coincide con `product`.
    # Si encuentra uno lo devuelve; si no, retorna `None` (gracias al valor por defecto de `next`).
    existing = next((p for p in inventory if p["Producto"] == product), None)
    if not existing:
        return False
    # Muestra un error, el producto ya existe en la lista
    print(f"Error: {product} ya existe en la lista.")
    # Le pregunta al usuario si desea modificar el producto existente (precio o cantidad)
    respuesta = input("Desea modificar precio o cantidad? (Si/No): ").strip().lower()
    # Si la respuesta es "si", modifica el precio y la cantidad
    if respuesta in ("si", "s"):
        # Llama a las funciones get_price() y get_quantity(), para poder modificarlos, además los guarda en su respectiva variable
        price = get_price()
        quantity = get_quantity()
        existing["Precio"] = price
        existing["Cantidad"] = quantity
        # El producto fue actualizado correctamente y imprime el nuevo precio y cantidad
        print(f"\n {product} actualizado correctamente.")
        print(f"  Precio: ${price:.2f}")
        print(f"  Cantidad: {quantity}")
    # Si la respuesta por el contario fue "no" no hace nada
    else:
        print(f"No se modificó {product}.")
    return True

# Función que pregunta al usuario si desea agregar otro producto
def ask_continue():
    while True:
        decision = input("Desea agregar otro producto? (Si/No): ").strip().lower()
        if decision in ("no", "n"):
            return False
        if decision in ("si", "s"):
            return True
        print("Opción no valida")

# Función que agrega el producto con ayuda de las funciones anteriores
def add_product():
    while True:
        product = get_product_name()
        if handle_existing_product(product):
            if ask_continue():
                continue
            return
        price = get_price()
        quantity = get_quantity()

        # Guarda los datos en un diccionario
        list_data = {
            "Producto": product,
            "Precio": price,
            "Cantidad": quantity,
        }

        # Agrega el datos del diccionario en la lista
        inventory.append(list_data)

        # Muestra el producto agregado correctamente
        print(f"\n {product} agregado correctamente.")
        print(f"  Precio: ${price:.2f}")
        print(f"  Cantidad: {quantity}")

        # Si la respuesta de ask_continue() es no, sale de la opción 1
        if not ask_continue():
            return
