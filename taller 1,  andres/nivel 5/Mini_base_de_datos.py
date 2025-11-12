# Mini base de datos.
# Diccionario donde se almacenarán los datos de los estudiantes.
# La clave será el nombre del estudiante y el valor será otro diccionario con su edad y promedio.
estudiantes = {}

# FUNCIÓN: agregar()
def agregar():
    # Solicita los datos básicos del estudiante.
    nombre = input("¿Cuál es tu nombre? ")
    edad = input("¿Cuántos años tienes? ")
    promedio = input("¿Cuál es tu promedio? ")
    # Guarda la información dentro del diccionario principal.
    estudiantes[nombre] = {"edad": edad, "promedio": promedio}
    print(f"El estudiante {nombre} ha sido agregado correctamente.")
    return

# FUNCIÓN: eliminar()
def eliminar():
    # Pide el nombre del estudiante que se desea eliminar.
    nombre = input("¿Qué estudiante vas a borrar? ")
    # Verifica si el estudiante existe en el diccionario.
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Se eliminó el estudiante {nombre} de la base de datos.")
    else:
        print(f"El estudiante {nombre} no está en la base de datos.")
    return

# FUNCIÓN: mostrar()
def mostrar():
    # Si el diccionario está vacío, no hay estudiantes registrados.
    if not estudiantes:
        print("Solo está DIOS aquí (no hay estudiantes).")
        return
    # Recorre todos los elementos del diccionario 'estudiantes'.
    for nombre, datos in estudiantes.items():
        print(f"El estudiante {nombre} tiene {datos['edad']} años y su promedio es {datos['promedio']}.")
    return

# MENÚ PRINCIPAL
while True:
    print("\nBienvenido a la escuela de mi compaaa")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Mostrar estudiantes")
    print("4. Salir")
    try:
        # Solicita al usuario que elija una opción del menú.
        opcion = int(input("¿Qué vas a hacer, mi compa? "))
        # Llama a la función correspondiente según la opción elegida.
        if opcion == 1:
            agregar()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            mostrar()
        elif opcion == 4:
            print("Mi compa, que Dios te bendiga.")
            break
        else:
            print("Mi compa, no entendí eso.")
    except ValueError:
        # Evita errores si el usuario escribe texto en lugar de número.
        print("Eso no es un número.")
        continue