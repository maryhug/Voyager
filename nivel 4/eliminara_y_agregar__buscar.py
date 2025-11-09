# 20 y 21, agregar y eliminar, buscar posicion en lista.
equipo = []
while repeti == True:
        print("  CREA TU PROPIO EQUIPO, DE NBA. ")
        print(" 1. agregar jugardor. ")
        print(" 2. eliminar jugador. ")
        print(" 3. ver planilla del equipo. ")
        print(" 4. ver posicion en la que esta el jugador.")
        print(" 5. salir del menu. ")
        try:
            draf = int(input(" ¿ Que haras ?. "))
            if draf == 1:
                print(".selecion de jugador. ")
                jugador = input("¿Que jugador deceas agragar?. ")
                equipo.append(jugador)
                print(f"Se agreago, el jugador {jugador}, a la planilla del equipo. ")
            elif draf == 2:
                print(".ELIMINACION DE JUGADOR. ")
                eliminado = input("¿con cual jugador, vas a cancelar contrato?. ")
                equipo.remove(eliminado)
                print(f"Se cancelo el contarrato, con el jugador, {eliminado}. Retirado de la planilla.")
            elif draf == 3: 
                print(".MOSTRANDO PLANILLA DE JUGADORES. ")
                print(equipo)
            elif draf == 4:
                print(".POSICION DE JUGADOR EN LA PLANILLA. ")  
                unidad = input("¿De que jugador, deceas saber su posicion en la planilla?. ")   
                posicion = equipo.index(unidad.lower())
                print(f"El jugador {unidad}, esta en la posicion {posicion + 1} de la planilla del equipo. ")
                
            elif draf == 5:
                repeti = False
                print("Saliendo del menu, hasta luego. ")
            else:
                print("MMMMEEEEEEHHHHHH........")

        except ValueError:
            print("mmmmeeeehhh....")