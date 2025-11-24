from crud import CRUD

crud = CRUD()
archivo = "datos.csv"

crud.crear_archivo(archivo)

while True:
    print("\n--- MENU ---")
    print("1. Crear persona")
    print("2. Listar personas")
    print("3. Actualizar persona")
    print("4. Eliminar persona")
    print("5. Exportar a TXT")
    print("6. Exportar a JSON")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        id_creado = crud.crear(archivo, nombre, edad)
        print(f"Persona creada con ID: {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        print("\n--- LISTADO ---")
        for fila in datos:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")

    elif opcion == "3":
        id_persona = input("ID a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_edad = input("Nueva edad: ")

        if crud.actualizar(archivo, id_persona, nuevo_nombre, nueva_edad):
            print("Persona actualizada correctamente.")
        else:
            print("No existe una persona con ese ID.")

    elif opcion == "4":
        id_persona = input("ID a eliminar: ")

        if crud.eliminar(archivo, id_persona):
            print("Persona eliminada correctamente.")
        else:
            print("No existe una persona con ese ID.")

    elif opcion == "5":
        crud.guardar_txt(archivo, "datos.txt")
        print("Exportado a datos.txt")

    elif opcion == "6":
        crud.guardar_json(archivo, "datos.json")
        print("Exportado a datos.json")

    elif opcion == "7":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")