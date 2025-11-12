# Agenda de contactos.
# Diccionario principal donde se guardarán los contactos
nokia = {}

# Función para pedir el nombre y número del contacto
def pedir():
    nombre = input(" Nombre del contacto: ")
    numero = input(" Número del contacto: ")
    return nombre, numero

# Función para agregar un nuevo contacto al diccionario
def agregar():
    nombre, numero = pedir()
    nokia[nombre] = numero
    if nombre in nokia:
        print(f"El contacto {nombre}: {numero} ha sido agregado exitosamente.")
    else:
        print(" mi compaaaa. ")
    return 

# Función para eliminar un contacto existente
def eliminar():
    print(" ¿Cuál contacto deseas eliminar?: ")
    nombre = input(" Nombre del contacto: ")
    if nombre in nokia:
        del nokia[nombre]
        print(f" El contacto {nombre} ha sido eliminado, my broo.")
    else:
        print(" Ese contacto no está en la lista, mi compaaa.")
    return

# Función para mostrar todos los contactos guardados
def mostrar():
    print(" Lista de contactos: ")
    if not nokia:
        print(" Mi compaaa, no hay nadie, solo está Dios. Siempre lo estará.")
        return 
    for nombre, numero in nokia.items():    
        print(nombre, ":", numero)

# Bucle principal del programa
while True:
    print(" Bienvenido a la agenda, mi compaaa. ")
    print(" 1. Agregar contacto. ")
    print(" 2. Eliminar contacto. ")
    print(" 3. Mostrar contactos. ")
    print(" 4. Salir. ")
    try:
        opcion = int(input(" ¿Qué vas a hacer, mi compa? "))
        if opcion == 1:
            agregar()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            mostrar()
        elif opcion == 4:
            print(" Gracias por usar la agenda, mi compaaa. Que Dios te bendiga. ")
            break
        else:
            print(" Mi compaaa, no entendí eso. ")
    except ValueError:
        print(" Meeeeeeehhh, eso no es un númeroooooooo heeeeehhhhhhh... ")
        continue