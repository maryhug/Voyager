# Gestión de estudiantes (mini base de datos).

estudiantes = []
siguiente_id = 1

def mostrar_menu_estudiantes():
    print("\n=== Gestión de Estudiantes ===")
    print("1) Agregar estudiante")
    print("2) Editar estudiante")
    print("3) Eliminar estudiante")
    print("4) Listar todos")
    print("5) Buscar por ID")
    print("6) Salir")

def leer_nota_valida(prompt):
    entrada = input(prompt).replace(',', '.').strip()
    while not (entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1):
        entrada = input("Nota inválida. Ingresa número (ej: 3.5): ").replace(',', '.').strip()
    return float(entrada)

while True:
    mostrar_menu_estudiantes()
    op = input("Elige una opción: ").strip()
    if op == "1":
        nombre = input("Nombre del estudiante: ").strip()
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()
        nota = leer_nota_valida("Nota (0-5): ")
        while nota < 0 or nota > 5:
            nota = leer_nota_valida("La nota debe estar entre 0 y 5. Ingresa de nuevo: ")
        estudiantes.append({"id": siguiente_id, "nombre": nombre, "nota": nota})
        print(f"Estudiante agregado con ID {siguiente_id}.")
        siguiente_id += 1
    elif op == "2":
        id_bus = input("ID del estudiante a editar: ").strip()
        if id_bus.isdigit():
            id_bus = int(id_bus)
            encontrado = False
            for e in estudiantes:
                if e["id"] == id_bus:
                    encontrado = True
                    print(f"Editando {e['nombre']} (nota {e['nota']})")
                    nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ").strip()
                    if nuevo_nombre:
                        e["nombre"] = nuevo_nombre
                    cambiar_nota = input("Cambiar nota? (s/n): ").strip().lower()
                    if cambiar_nota == "s":
                        nueva_n = leer_nota_valida("Nueva nota (0-5): ")
                        while nueva_n < 0 or nueva_n > 5:
                            nueva_n = leer_nota_valida("La nota debe estar entre 0 y 5. Ingresa de nuevo: ")
                        e["nota"] = nueva_n
                    print("Estudiante actualizado.")
                    break
            if not encontrado:
                print("ID no encontrado.")
        else:
            print("ID inválido.")
    elif op == "3":
        id_bus = input("ID del estudiante a eliminar: ").strip()
        if id_bus.isdigit():
            id_bus = int(id_bus)
            for i, e in enumerate(estudiantes):
                if e["id"] == id_bus:
                    confirm = input(f"Eliminar {e['nombre']}? (s/n): ").strip().lower()
                    if confirm == "s":
                        estudiantes.pop(i)
                        print("Estudiante eliminado.")
                    else:
                        print("Eliminación cancelada.")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")
    elif op == "4":
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for e in estudiantes:
                print(f"ID {e['id']} - {e['nombre']} - Nota: {e['nota']:.1f}")
    elif op == "5":
        id_bus = input("ID a buscar: ").strip()
        if id_bus.isdigit():
            id_bus = int(id_bus)
            for e in estudiantes:
                if e["id"] == id_bus:
                    print(f"Encontrado: ID {e['id']} - {e['nombre']} - Nota: {e['nota']:.1f}")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")
    elif op == "6":
        print("Saliendo de gestión de estudiantes.")
        break
    else:
        print("Opción inválida.")

