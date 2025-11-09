# Agenda de contactos (lista de diccionarios).

# Lista que almacena todos los contactos
agenda = []
# Variable que controla el ID único autoincremental para cada contacto
siguiente_id = 1

# Muestra el menú principal de la agenda de contactos.
def menu_agenda():
    print("\n=== Agenda de Contactos ===")
    print("1) Agregar contacto")
    print("2) Buscar por nombre")
    print("3) Editar contacto")
    print("4) Eliminar contacto")
    print("5) Listar contactos")
    print("6) Salir")

# Busca contactos cuyo nombre contenga el texto especificado.
def buscar_por_nombre(texto):
    texto = texto.lower()
    return [c for c in agenda if texto in c["nombre"].lower()]

while True:
    menu_agenda()
    opcion = input("Elige opción: ").strip()

    # Opción 1: Agregar nuevo contacto
    if opcion == "1":
        # Solicitar nombre con validación de campo vacío
        nombre = input("Nombre: ").strip()
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()
        # Solicitar teléfono y email (pueden estar vacíos)
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        # Agregar contacto a la agenda con ID único
        agenda.append({"id": siguiente_id, "nombre": nombre, "telefono": telefono, "email": email})
        print(f"Contacto agregado con ID {siguiente_id}.")
        # Incrementar el ID para el próximo contacto
        siguiente_id += 1

    # Opción 2: Buscar contacto por nombre (búsqueda parcial)
    elif opcion == "2":
        # Solicitar término de búsqueda
        parte_nombre = input("Nombre o parte del nombre a buscar: ").strip()
        # Llamar a la función de búsqueda
        resultados = buscar_por_nombre(parte_nombre)
        # Mostrar resultados encontrados
        if resultados:
            for c in resultados:
                print(f"ID {c['id']} - {c['nombre']} - {c['telefono']} - {c['email']}")
        else:
            print("No se encontraron coincidencias.")

    # Opción 3: Editar un contacto existente
    elif opcion == "3":
        # Solicitar el ID del contacto a editar
        id_buscar = input("ID del contacto a editar: ").strip()
        # Validar que el ID sea un número
        if id_buscar.isdigit():
            id_buscar = int(id_buscar)
            # Buscar el contacto por ID
            for c in agenda:
                if c["id"] == id_buscar:
                    # Permitir editar nombre (opcional, mantiene el anterior si se presiona Enter)
                    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{c['nombre']}'): ").strip()
                    if nuevo_nombre:
                        c["nombre"] = nuevo_nombre
                    # Permitir editar teléfono (opcional)
                    nuevo_tel = input(f"Nuevo teléfono (Enter para mantener '{c['telefono']}'): ").strip()
                    if nuevo_tel:
                        c["telefono"] = nuevo_tel
                    # Permitir editar email (opcional)
                    nuevo_email = input(f"Nuevo email (Enter para mantener '{c['email']}'): ").strip()
                    if nuevo_email:
                        c["email"] = nuevo_email
                    print("Contacto actualizado.")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")

    # Opción 4: Eliminar un contacto
    elif opcion == "4":
        # Solicitar el ID del contacto a eliminar
        id_buscar = input("ID del contacto a eliminar: ").strip()
        # Validar que el ID sea un número
        if id_buscar.isdigit():
            id_buscar = int(id_buscar)
            # Buscar el contacto por ID usando enumerate para obtener el índice
            for i, c in enumerate(agenda):
                if c["id"] == id_buscar:
                    # Confirmar antes de eliminar
                    confirm = input(f"Eliminar {c['nombre']}? (s/n): ").strip().lower()
                    if confirm == "s":
                        # pop(i) elimina el contacto en la posición i
                        agenda.pop(i)
                        print("Contacto eliminado.")
                    else:
                        print("Eliminación cancelada.")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")

    # Opción 5: Listar todos los contactos
    elif opcion == "5":
        if not agenda:
            print("Agenda vacía.")
        else:
            # Iterar sobre todos los contactos
            for c in agenda:
                print(f"ID {c['id']} - {c['nombre']} - {c['telefono']} - {c['email']}")

    # Opción 6: Salir del programa
    elif opcion == "6":
        print("Saliendo de la agenda.")
        break

    # Opción inválida
    else:
        print("Opción inválida.")
