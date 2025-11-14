# Función verifica que en la lista haya algún producto
def any_products (products):
    # No hay productos en la lista
    if not products:
        print("No hay productos registrados.")
        return False
    # Si hay productos
    return True

# Función que calcula el total del inventario
def total_inventory(products):
    # Llama al función para confirmar si hay productos
    if not any_products(products):
        return 0.0

    total = 0
    # For que recorre la lista
    for p in products:
        try:
            # .get toma el precio y la cantidad de los productos (uno por uno)
            price = float(p.get("Precio", 0))
            qty = int(p.get("Cantidad", 0))
            total += price * qty
        # Errores a la hora de hacer el total por datos mal ingresados o no compatibles
        except (ValueError, TypeError):
            print(f"Advertencia: datos inválidos en el producto: {p}")
    # Muestra y retorna el total del inventario
    print(f"Valor total del inventario: ${total:.2f}")
    return total

# Función que muestra el total de productos ingresados
def  total_registered_products(products):
    # Llama al función para confirmar si hay productos
    if not any_products(products):
        return 0
    # Si hay productos recorre la lista y toma la longitud de la lista
    print(f"Cantidad de productos registrados: {len(products)}")
    # Retorna el valor obtenido
    return len(products)