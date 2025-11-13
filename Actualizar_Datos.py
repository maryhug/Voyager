#Modulo para actualizar datos de pacientes
#Autor: [santiago rendon sierra]

def actualizar_paciente(pacientes):
    """
    Funcion para actualizar los datos de un paciente
    """
    print("\n--- ACTUALIZAR PACIENTE ---")

    #verificar si hay pacientes
    if len(pacientes) == 0:
        print("No hay pscientes registrados")
        return
    
    #pedir el id del paciente
    id_buscar = int(input("Ingrese el id del paciente: "))

    #Buscar el paciente
    paciente_encontrado = None
    for paciente in pacientes :
        if paciente["id"] == id_buscar:
            paciente_encontrado = paciente 
            break

    #si no existe el paciente
    if paciente_encontrado == None:
        print("paciente no encontrado")
        return
    
    #Mostrar datos actuales
    print("\nDatos actuales:")
    print("Nombre:", paciente_encontrado["nombre"])
    print("Edad:", paciente_encontrado["edad"])
    print("Diagnostico:", paciente_encontrado["diagnostico"])
    print("Historial:", paciente_encontrado["historial"])

    #Menu de opciones
    print("\n¿Que desas actualizar?")
    print("1. Edad")
    print("2. Diagnostico")
    print("3. Agregar  evento al historial")

    opcion = input("seleccione opcion (1-3): ")

    #Actualizar segunla opcion
    if opcion == "1":
        #Actualizar edad
        nueva_edad = int(input("ingrese la nueva edad:" ))
        paciente_encontrado["edad"] = nueva_edad
        print("Edad actualizada con exito")

    elif opcion == "2":
        #Actualizar diagnostico
        nuevo_diagnostico = input("Ingrese el nuevo diagnostico: ")
        paciente_encontrado["diagnostico"] = nuevo_diagnostico
        print("diagnostico actualizado con exito ")

    elif opcion == "3":
        #Agregar al historial
        nuevo_evento = input("Ingrese el nuevo evento: ")
        paciente_encontrado["historial"].append(nuevo_evento)
        print("Evento agregado al historial con exito")

    else: 
        print("opcion no valida")

    #mostrar datos actualizados
    print("\nDatos actualizados:")
    print("Nombre:",paciente_encontrado["nombre"])
    print("Edad:",paciente_encontrado["edad"])
    print("Diagnostico:",paciente_encontrado["diagnostico"])
    print("Historial:",paciente_encontrado["historial"])

if __name__ == "__main__":
    # Lista de prueba
    pacientes = [
        {
            "id": 1,
            "nombre": "Carlos Pérez",
            "edad": 45,
            "genero": "Masculino",
            "diagnostico": "Hipertensión",
            "historial": ["Consulta general", "Control presión"]
        }
    ]



    actualizar_paciente(pacientes)    