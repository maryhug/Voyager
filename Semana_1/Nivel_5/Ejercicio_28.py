# Gestión de estudiantes (mini base de datos).

# Lista que almacena todos los estudiantes
estudiantes = []

# Variable que controla el ID único autoincremental para cada estudiante
siguiente_id = 1

# Muestra el menú principal de gestión de estudiantes.
def mostrar_menu_estudiantes():
    print("\n=== Gestión de Estudiantes ===")
    print("1) Agregar estudiante")
    print("2) Editar estudiante")
    print("3) Eliminar estudiante")
    print("4) Listar todos")
    print("5) Buscar por ID")
    print("6) Salir")

# Solicita y valida una nota numérica.
def leer_nota_valida(prompt):
    entrada = input(prompt).replace(',', '.').strip()
    # Bucle de validación: continúa hasta recibir un número válido
    while not (entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1):
        entrada = input("Nota inválida. Ingresa número (ej: 3.5): ").replace(',', '.').strip()
    return float(entrada)

# Opciones del menú
while True:
    mostrar_menu_estudiantes()
    opcion = input("Elige una opción: ").strip()

    # Opción 1: Agregar un nuevo estudiante
    if opcion == "1":
        # Solicitar nombre con validación de campo vacío
        nombre = input("Nombre del estudiante: ").strip()
        while nombre == "":
            nombre = input("Nombre no puede estar vacío. Ingresa de nuevo: ").strip()

        # Solicitar nota usando la función de validación
        nota = leer_nota_valida("Nota (0-5): ")
        # Validar que la nota esté en el rango permitido (0-5)
        while nota < 0 or nota > 5:
            nota = leer_nota_valida("La nota debe estar entre 0 y 5. Ingresa de nuevo: ")
        # Agregar estudiante a la lista con ID único
        estudiantes.append({"id": siguiente_id, "nombre": nombre, "nota": nota})
        print(f"Estudiante agregado con ID {siguiente_id}.")
        # Incrementar el ID para el próximo estudiante
        siguiente_id += 1

    # Opción 2: Editar un estudiante existente
    elif opcion == "2":
        # Solicitar el ID del estudiante a editar
        id_buscar = input("ID del estudiante a editar: ").strip()

        # Validar que el ID sea un número
        if id_buscar.isdigit():
            id_buscar = int(id_buscar)
            encontrado = False
            # Buscar el estudiante por ID en la lista
            for e in estudiantes:
                if e["id"] == id_buscar:
                    encontrado = True
                    print(f"Editando {e['nombre']} (nota {e['nota']})")
                    # Permitir cambiar el nombre (opcional)
                    nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ").strip()
                    if nuevo_nombre:
                        e["nombre"] = nuevo_nombre
                    # Preguntar si desea cambiar la nota
                    cambiar_nota = input("Cambiar nota? (s/n): ").strip().lower()
                    if cambiar_nota == "s":
                        nueva_nota = leer_nota_valida("Nueva nota (0-5): ")
                        # Validar que la nueva nota esté en el rango permitido
                        while nueva_nota < 0 or nueva_nota > 5:
                            nueva_nota = leer_nota_valida("La nota debe estar entre 0 y 5. Ingresa de nuevo: ")
                        e["nota"] = nueva_nota
                    print("Estudiante actualizado.")
                    # Salir del bucle una vez encontrado y editado
                    break
            # Si el ID no se encontró en la lista
            if not encontrado:
                print("ID no encontrado.")
        else:
            print("ID inválido.")

    # Opción 3: Eliminar un estudiante
    elif opcion == "3":
        # Solicitar el ID del estudiante a eliminar
        id_buscar = input("ID del estudiante a eliminar: ").strip()
        # Validar que el ID sea un número
        if id_buscar.isdigit():
            id_buscar = int(id_buscar)
            # Buscar el estudiante por ID usando enumerate para obtener el índice
            for i, e in enumerate(estudiantes):
                if e["id"] == id_buscar:
                    # Confirmar antes de eliminar
                    confirm = input(f"Eliminar {e['nombre']}? (s/n): ").strip().lower()
                    if confirm == "s":
                        # pop(i) elimina el estudiante en la posición i
                        estudiantes.pop(i)
                        print("Estudiante eliminado.")
                    else:
                        print("Eliminación cancelada.")
                    break    # Salir del bucle una vez encontrado
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")

    # Opción 4: Listar todos los estudiantes
    elif opcion == "4":
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            # Iterar sobre todos los estudiantes
            for e in estudiantes:
                # Mostrar información formateada con 1 decimal para la nota
                print(f"ID {e['id']} - {e['nombre']} - Nota: {e['nota']:.1f}")

    # Opción 5: Buscar un estudiante por ID
    elif opcion == "5":
        # Solicitar el ID a buscar
        id_buscar = input("ID a buscar: ").strip()
        # Validar que el ID sea un número
        if id_buscar.isdigit():
            id_buscar = int(id_buscar)
            # Buscar el estudiante por ID
            for e in estudiantes:
                if e["id"] == id_buscar:
                    print(f"Encontrado: ID {e['id']} - {e['nombre']} - Nota: {e['nota']:.1f}")
                    break
            else:
                print("ID no encontrado.")
        else:
            print("ID inválido.")

    # Opción 6: Salir del programa
    elif opcion == "6":
        print("Saliendo de gestión de estudiantes.")
        break

    # Opción inválida
    else:
        print("Opción inválida.")