#Simular que la lista ya tiene los pacientes agregados
lista = []
paciente1 = {
    "nombre": "Samuel Ocampo",
    "id": 1,
    "diagnostico": "Gripe común"
}
paciente2 = {
    "nombre": "Samuel García",
    "id": 2,
    "diagnostico": "Hipertensión"
}
paciente3 = {
    "nombre": "Carlos López",
    "id": 3,
    "diagnostico": "Diabetes"
}
lista.append(paciente1)
lista.append(paciente2)
lista.append(paciente3)

#Función para buscar los pacientes
def buscar_pacientes():

    #Bucle que se repita hasta que el usuario decida no buscar más pacientes o ingrese un 4
    while True:
        print("\nBÚSQUEDA DE PACIENTES")
        print("\n1. Buscar por Nombre (parcial o completo)")
        print("2. Buscar por ID")
        print("3. Buscar por Diagnóstico")
        print("4. Volver al menú principal")
        
        #Verificar que ingrese un número entero
        try:
            opcion = int(input("\nSeleccione una opción (1-4): "))
        except ValueError:
            print("\nPor favor ingrese un número válido.")
            continue
        
        #Dependiendo de cómo decida buscar al paciente (nombre, ID o diagnóstico), usar funciones para cada opción
        if opcion == 1:
            buscar_nombre()
        elif opcion == 2:
            buscar_id()
        elif opcion == 3:
            buscar_diagnostico()
        elif opcion == 4:
            print("\nVolviendo al menú principal...")
            break

        #Verificar que ingrese una opción válida
        else:
            print("\nOpción no válida. Por favor seleccione 1-4.")
            continue
        
        #Si hizo una busqueda exitosa, preguntar si desea buscar otro paciente dentro de un bucle
        if opcion in [1, 2, 3]:
            while True:
                respuesta = input("\n¿Desea realizar otra búsqueda? (si/no): ").lower()
                if respuesta == 'si':
                    break
                elif respuesta == 'no':
                    print("\nSaliendo del módulo de búsqueda...")
                    return
                
                #Verificar que ingrese una opción válida
                else:
                    print("\nPor favor responda (si/no).")

#Función para buscar al paciente por el nombre
def buscar_nombre():

    #Verificar que la lista si tenga pacientes registrados
    if not lista:
        print("\nNo hay pacientes registrados en el sistema.")
        return
        
    nombre_buscar = input("\nDigite el nombre del paciente (parcial o completo): ").capitalize()
    
    #Verificar que el usuario no deje vacío el nombre
    if not nombre_buscar:
        print("\nDebe ingresar un nombre para buscar.")
        return
    
    #Lista vacía para ir ingresando los pacientes que tengan el mismo nombre
    pacientes_encontrados = []
    
    #Recorrer la lista orifginal para ingresar los nombres repetidos a la lista vacía
    for paciente in lista:
        if nombre_buscar in paciente['nombre']:
            pacientes_encontrados.append(paciente)

    #Si el nombre coincide, imprimir los datos de los pacientes encontrados
    if pacientes_encontrados:
        print(f"\nSe encontraron {len(pacientes_encontrados)} pacientes:")
        for i in range(len(pacientes_encontrados)):
            print(f"\nPaciente {i + 1}:")

            #Función para imprimir los datos del paciente
            mostrar_datos_paciente(pacientes_encontrados[i])
    else:
        print(f"\nNo se encontraron pacientes con el nombre: {nombre_buscar}")

#Función para buscar al paciente por el ID
def buscar_id():

    #Verificar que la lista si tenga pacientes registrados
    if not lista:
        print("\nNo hay pacientes registrados en el sistema")
        return
    
    #Verificar que el usuario ingrese un número entero
    try:
        id_buscar = int(input("\nDigite el ID del paciente: "))
    except ValueError:
        print("\nEl ID debe ser un número entero")
        return
    #Si el ID coincide, imprimir los datos del paciente encontrado
    for paciente in lista:
        if paciente['id'] == id_buscar:
            print("\nPaciente encontrado:")

            #Función para imprimir los datos del paciente
            mostrar_datos_paciente(paciente)
            return
    
    print(f"\nNo se encontró ningún paciente con ID: {id_buscar}")

#Función para buscar al paciente por el diagnóstico
def buscar_diagnostico():

    #Verificar que la lista si tenga pacientes registrados
    if not lista:
        print("\nNo hay pacientes registrados en el sistema.")
        return
        
    diagnostico_buscar = input("\nDigite el diagnóstico a buscar: ").capitalize()
    
    #Verificar que el usuario no deje vacío el diagnóstico
    if not diagnostico_buscar:
        print("\nDebe ingresar un diagnóstico para buscar.")
        return
    
    #Lista vacía para ir ingresando los pacientes que tengan el mismo diagnóstico
    pacientes_encontrados = []
    
    #Recorrer la lista orifginal para ingresar los pacientes con el mismo diagnóstico a la lista vacía
    for paciente in lista:
        if diagnostico_buscar in paciente['diagnostico']:
            pacientes_encontrados.append(paciente)
    
    #Si el diagnóstico coincide, imprimir los datos de los pacientes encontrados
    if pacientes_encontrados:
        print(f"\nSe encontraron {len(pacientes_encontrados)} pacientes:")
        for i in range(len(pacientes_encontrados)):
            print(f"\nPaciente {i + 1}:")

            #Función para imprimir los datos del paciente
            mostrar_datos_paciente(pacientes_encontrados[i])
    else:
        print(f"No se encontraron pacientes con diagnóstico: {diagnostico_buscar}")

#Función para mostrar los datos del paciente
def mostrar_datos_paciente(paciente):
    print(f"Nombre: {paciente['nombre']}")
    print(f"ID: {paciente['id']}")
    print(f"Diagnóstico: {paciente['diagnostico']}")

#Simular el llamado de la función al menú principal del código
buscar_pacientes()
