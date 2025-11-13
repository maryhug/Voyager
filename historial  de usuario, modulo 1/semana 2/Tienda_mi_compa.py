inventario = {" leyes_del_poder. " : 12000,}
carrito = []
def agregar_al_carrito(producto, cantidad):
    for precio, in inventario.items(producto):
        carrito.append(producto["precio"] )
        total_producto = cantidad * precio
        productos_totales = sum(cantidad)
    return print(f"---{producto}---{cantidad}---{precio}-//-{total_producto}")
      
      
agregar_al_carrito("leyes del poder", "4")