# Agenda de contactos (lista de diccionarios).

agenda = []
siguiente_id = 1

def menu_agenda():
    print("\n=== Agenda de Contactos ===")
    print("1) Agregar contacto")
    print("2) Buscar por nombre")
    print("3) Editar contacto")
    print("4) Eliminar contacto")
    print("5) Listar contactos")
    print("6) Salir")

def buscar_por_nombre(texto):
    texto = texto.lower()
    return [c for c in agenda if texto in c["nombre"].lower()]

while True:
    menu_agenda()
    op = input("Elige opción: ").strip()
    if op == "1":
        nombre = input("Nombre: ").strip()
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        agenda.append({"id": siguiente_id, "nombre": nombre, "telefono": telefono, "email": email})
        print(f"Contacto agregado con ID {siguiente_id}.")
        siguiente_id += 1
    elif op == "2":
        q = input("Nombre o parte del nombre a buscar: ").strip()
        resultados = buscar_por_nombre(q)
        if resultados:
            for c in resultados:
                print(f"ID {c['id']} - {c['nombre']} - {c['telefono']} - {c['email']}")
        else:
            print("No se encontraron coincidencias.")
    elif op == "3":
        id_bus = input("ID del contacto a editar: ").strip()
        if id_bus.isdigit():
            id_bus = int(id_bus)
            for c in agenda:
                if c["id"] == id_bus:
                    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{c['nombre']}'): ").strip()
                    if nuevo_nombre:
                        c["nombre"] = nuevo_nombre
                    nuevo_tel = input(f"Nuevo teléfono (Enter para mantener '{c['telefono']}'): ").strip()
                    if nuevo_tel:
                        c["telefono"] = nuevo_tel
                    nuevo_email = input(f"Nuevo email (Enter para mantener '{c['email']}'): ").strip()
                    if nuevo_email:
                        c["email"] = nuevo_email
                    print("Contacto actualizado.")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")
    elif op == "4":
        id_bus = input("ID del contacto a eliminar: ").strip()
        if id_bus.isdigit():
            id_bus = int(id_bus)
            for i, c in enumerate(agenda):
                if c["id"] == id_bus:
                    confirm = input(f"Eliminar {c['nombre']}? (s/n): ").strip().lower()
                    if confirm == "s":
                        agenda.pop(i)
                        print("Contacto eliminado.")
                    else:
                        print("Eliminación cancelada.")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")
    elif op == "5":
        if not agenda:
            print("Agenda vacía.")
        else:
            for c in agenda:
                print(f"ID {c['id']} - {c['nombre']} - {c['telefono']} - {c['email']}")
    elif op == "6":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida.")
