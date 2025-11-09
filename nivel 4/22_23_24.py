# promedio de numeros, saltar numeros pares y eliminar duplicados
# Lista principal donde se guardarán todos los números ingresados
todos_los_numeros = []

while True:
    # Menú principal del programa
    print("  CREA TU LISTA DE NÚMEROS.COM ")
    print(" 1. Agregar número. ")
    print(" 2. Eliminar número. ")
    print(" 3. Ver lista de números. ")
    print(" 4. Ver posición en la que está el número. ")
    print(" 5. Calcular promedio de números. ")
    print(" 6. Opciones de creación de listas. ")
    print(" 7. Eliminar duplicados de la lista. ")
    print(" 8. Salir del menú. ")

    try:
        draf = int(input(" ¿Qué harás? "))
        
        # Opción 1: Agregar número a la lista
        if draf == 1:
            print(".AGREGAR. ")
            op1 = int(input("¿Qué número vas a agregar? "))
            todos_los_numeros.append(op1)
            print(f"Se agregó el número {op1} a la lista de números. ")

        # Opción 2: Eliminar número de la lista
        elif draf == 2:
            print(".ELIMINACIÓN DE NÚMEROS. ")
            op2 = int(input("¿Qué número deseas eliminar? "))
            if op2 not in todos_los_numeros:
                print("El número no está en la lista. ")
            else:    
                todos_los_numeros.remove(op2)
                print(f"Se eliminó el número {op2} de la lista.")

        # Opción 3: Mostrar todos los números de la lista
        elif draf == 3: 
            print(".MOSTRANDO LISTA DE NÚMEROS. ")
            print(f"Lista de números: {todos_los_numeros}. ")

        # Opción 4: Buscar la posición de un número específico
        elif draf == 4:
            print(".POSICIÓN DE NÚMEROS. ")  
            unidad = int(input("¿De qué número deseas saber su posición en la lista? "))
            if unidad not in todos_los_numeros:
                print("El número no está en la lista. ")
            else:
                posicion = todos_los_numeros.index(unidad)
                print(f"El número {unidad} está en la posición {posicion + 1} de la lista. ")

        # Opción 5: Calcular promedio de números
        elif draf == 5:
            print(" CALCULO DE PROMEDIO. ")
            n = int(input("¿De cuántos números va a ser el promedio? "))
            suma = 0
            R = 0
            total = []
            for i in range(n):
                dupla = float(input(f"Dime el número {i + 1}: "))
                total.append(dupla)
                suma += dupla 
            R = suma / n  
            print(f"El promedio de los números {total} es {R}. ")  

        # Opción 6: Submenú para crear listas automáticas
        elif draf == 6:
            print(" 1. Lista sin números pares. ")
            print(" 2. Lista sin números impares. ")
            print(" 3. Lista con todos los números. ")
            print(" 4. Salir del menú. ")
            while True:
                try:
                    opcion = int(input(" ¿Qué deseas hacer? ")) 
                    
                    # Lista sin números pares
                    if opcion == 1:
                        print("Lista sin números pares. ")
                        m = int(input("¿Hasta qué número deseas hacer la lista? "))
                        galaga = [i for i in range(0, m + 1) if i % 2 != 0]
                        todos_los_numeros.extend(galaga)
                        print(galaga)

                    # Lista sin números impares
                    elif opcion == 2:
                        print("Lista sin números impares.")
                        l = int(input("¿Hasta qué número deseas hacer la lista? "))
                        pacman = [i for i in range(0, l + 1) if i % 2 == 0]
                        todos_los_numeros.extend(pacman)
                        print(pacman)

                    # Lista con todos los números
                    elif opcion == 3:
                        print("Lista con todos los números. ")
                        ñ = int(input("¿Hasta qué número deseas hacer la lista? "))  
                        tetris = [i for i in range(0, ñ + 1)]
                        todos_los_numeros.extend(tetris)
                        print(tetris)   

                    # Salir del submenú
                    elif opcion == 4:
                        print("Saliendo del menú de creación de listas. ")
                        break

                    else:
                        print("MMMMEEEEEEHHHHHH........")             

                except ValueError:
                    print("mmmmeeeehhh....")  
                    continue

        # Opción 7: Eliminar números duplicados de la lista
        elif draf == 7:
            print("Eliminar duplicados de lista. ")
            no_mas_pares_iguales = list(set(todos_los_numeros))
            print(f"Lista sin duplicados: {no_mas_pares_iguales}. ")

        # Opción 8: Salir del programa
        elif draf == 8:
            print("Saliendo del menú, hasta luego. ")
            break

        # Opción no válida
        else:
            print("MMMMEEEEEEHHHHHH........")

    # Control de errores si el usuario escribe letras en lugar de números
    except ValueError:
        print("mmmmeeeehhh....")