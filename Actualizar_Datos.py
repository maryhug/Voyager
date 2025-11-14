# Modulo para actualizar datos de pacientes
# Autor: [Santiago Rendón Sierra]

def actualizar_paciente(pacientes):
    # Funcion para actualizar los datos de un paciente
    print("\n--- ACTUALIZAR PACIENTE ---")

    # verificar si hay pacientes
    if len(pacientes) == 0:
        print("No hay pacientes registrados")
        return

    #  CAMBIO: Bucle para reintentar si el ID no existe
    while True:
        # Validar que el usuario ingrese un número
        try:
            id_buscar = int(input("Ingrese el id del paciente: "))
        except ValueError:
            print(" Por favor ingrese un número válido")
            continue  # Volver a preguntar

        # Buscar el paciente
        paciente_encontrado = None
        for paciente in pacientes:
            if paciente["ID"] == id_buscar:
                paciente_encontrado = paciente
                break

        # si no existe el paciente
        if paciente_encontrado == None:
            print(f"❌ No se encontró paciente con ID: {id_buscar}")
            # Preguntar si quiere intentar de nuevo
            reintentar = input("¿Desea intentar con otro ID? (s/n): ").lower()
            if reintentar != 's':
                return  # Salir de la función
            # Si responde 's', el bucle while continúa
        else:
            #  Si encontró el paciente, salir del bucle
            break

    # Normalizar Historial a lista si no lo es (compatibilidad)
    historial_actual = paciente_encontrado.get("Historial", [])
    if not isinstance(historial_actual, list):
        paciente_encontrado["Historial"] = [historial_actual] if historial_actual else []

    # Mostrar datos actuales
    print("\nDatos actuales:")
    print("Nombre:", paciente_encontrado["Nombre_completo"])
    print("Edad:", paciente_encontrado["Edad"])
    print("Diagnostico:", paciente_encontrado["Diagnostico"])
    print("Historial:", paciente_encontrado["Historial"])

    # Menu de opciones
    print("\n¿Que desas actualizar?")
    print("1. Edad")
    print("2. Diagnostico")
    print("3. Agregar  evento al historial")

    opcion = input("seleccione opcion (1-3): ")

    # Actualizar segunla opcion
    if opcion == "1":
        # Actualizar edad
        nueva_edad = int(input("ingrese la nueva edad:"))
        paciente_encontrado["Edad"] = nueva_edad
        print("Edad actualizada con exito")

    elif opcion == "2":
        # Actualizar diagnostico
        nuevo_diagnostico = input("Ingrese el nuevo diagnostico: ")
        paciente_encontrado["Diagnostico"] = nuevo_diagnostico
        print("diagnostico actualizado con exito ")

    elif opcion == "3":
        # Agregar al historial
        nuevo_evento = input("Ingrese el nuevo evento: ")
        paciente_encontrado["Historial"].append(nuevo_evento)
        print("Evento agregado al historial con éxito")

    else:
        print("Opción no valida")

    # mostrar datos actualizados
    print("\nDatos actualizados:")
    print("Nombre:", paciente_encontrado["Nombre_completo"])
    print("Edad:", paciente_encontrado["Edad"])
    print("Diagnostico:", paciente_encontrado["Diagnostico"])
    print("Historial:", paciente_encontrado["Historial"])
