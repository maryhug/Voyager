# Importa los metodos add_product, inventory y todos los metodos de la clase Calculate_Statistics
# Para poder utilizarlos aquí
from Function.Add import add_product, inventory
from Function.Calculate_Statistics import *

# Función que muestra los productos ingresados
def result():
    print("Resultado:")
    for i, prod in enumerate(inventory, 1):
        print(f"Producto {i}: {prod}")

# Función para separar las opciones del resultado
def decorator():
    print("-" * 25)
    print()

# Función que muestra las opciones del menú
def display_menu():
    print("Menu:")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Calcular Estadísticas")
    print("4. Salir")

# Función del menú
def main():
    # Se declara salida en True, por si alguna vez salida es False sale del programa
    salida = True
    while salida:
        print()
        display_menu()
        try:
            # Pide al usuario que desea hacer
            opcion = int(input("Ingrese su opción: "))
        # No ingreso ninguna de las opciones validas
        except ValueError:
            print("Opción no válida")
            continue
        decorator()
        # Llama a la función agregar producto
        if opcion == 1:
            add_product()
            decorator()
        elif opcion == 2:
            # Llama a la función mostrar productos
            result()
            decorator()
        elif opcion == 3:
            # Llama a la función estadísticas de los productos
            total_registered_products(inventory)
            total_inventory(inventory)
        elif opcion == 4:
            # Sale del programa, se declaró salida en False
            print("Bye")
            salida = False
        else:
            # No ingreso ninguna de las opciones validas
            print("Opción no valida")

if __name__ == "__main__":
    main()