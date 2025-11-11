# 20 y 21, agregar y eliminar, buscar posicion en lista.
# Lista que contendrá los jugadores del equipo
equipo = []

# Variable de control del bucle principal
repeti = True

while repeti:
    # Menú principal
    print("  CREA TU PROPIO EQUIPO, DE NBA. ")
    print(" 1. agregar jugador. ")
    print(" 2. eliminar jugador. ")
    print(" 3. ver planilla del equipo. ")
    print(" 4. ver posición en la que está el jugador.")
    print(" 5. salir del menú. ")

    try:
        # Solicita al usuario qué acción desea realizar
        draf = int(input(" ¿Qué harás? "))

        # Opción 1: agregar jugador
        if draf == 1:
            print(".selección de jugador. ")
            jugador = input("¿Qué jugador deseas agregar? ")
            equipo.append(jugador)
            print(f"Se agregó el jugador {jugador} a la planilla del equipo. ")

        # Opción 2: eliminar jugador
        elif draf == 2:
            print(".ELIMINACIÓN DE JUGADOR. ")
            eliminado = input("¿Con cuál jugador vas a cancelar contrato? ")
            if eliminado in equipo:
                equipo.remove(eliminado)
                print(f"Se canceló el contrato con el jugador {eliminado}. Retirado de la planilla.")
            else:
                print(f"El jugador {eliminado} no está en la planilla.")

        # Opción 3: mostrar planilla
        elif draf == 3: 
            print(".MOSTRANDO PLANILLA DE JUGADORES. ")
            print(equipo)

        # Opción 4: ver posición de un jugador
        elif draf == 4:
            print(".POSICIÓN DE JUGADOR EN LA PLANILLA. ")  
            unidad = input("¿De qué jugador deseas saber su posición en la planilla? ")
            if unidad in equipo:
                posicion = equipo.index(unidad)
                print(f"El jugador {unidad} está en la posición {posicion + 1} de la planilla del equipo.")
            else:
                print(f"El jugador {unidad} no se encuentra en la planilla.")

        # Opción 5: salir del menú
        elif draf == 5:
            repeti = False
            print("Saliendo del menú, hasta luego. ")

        # Opción inválida
        else:
            print("MMMMEEEEEEHHHHHH........")

    # Captura errores si el usuario ingresa algo que no sea número
    except ValueError:
        print("mmmmeeeehhh....")