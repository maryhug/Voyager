# Imprime los campos de un paciente.
def imprimir_paciente(p):
    if not p:
        print("Paciente vacío o None.")
        return
    print("-" * 40)
    print(f"ID: {p.get('ID')}")
    print(f"Nombre: {p.get('Nombre_completo')}")
    print(f"Género: {p.get('Genero')}")
    print(f"Diagnóstico: {p.get('Diagnostico')}")
    print(f"Historial: {p.get('Historial')}")
    print(f"Edad: {p.get('Edad')}")
    print("-" * 40)

# Elimina el paciente cuya clave "ID" coincida con id_buscar.
# Devuelve el diccionario del paciente eliminado o None (si no se encontró o se canceló).
def eliminar_paciente_por_id(lista_pacientes, id_buscar, pedir_confirmacion=True):
    id_str = str(id_buscar).strip()
    for i, p in enumerate(lista_pacientes):
        if str(p.get("ID")) == id_str:
            print("Paciente encontrado:")
            imprimir_paciente(p)
            if pedir_confirmacion:
                resp = input("¿Confirmas eliminar este paciente? (s/n): ").strip().lower()
                if resp not in ("s", "si", "y", "yes"):
                    print("Eliminación cancelada.")
                    return None
            eliminado = lista_pacientes.pop(i)
            print(f"Paciente con ID {id_buscar} eliminado.")
            return eliminado
    print(f"No se encontró paciente con ID {id_buscar}.")
    return None