from collections import Counter
from Clinic.Delete import imprimir_paciente

# Imprime todos los pacientes de la lista.
def reporte_todos_los_pacientes(lista_pacientes):
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return
    print("\n=== Todos los pacientes ===")
    for p in lista_pacientes:
        imprimir_paciente(p)

def reporte_cantidad_total(lista_pacientes):
    total = len(lista_pacientes)
    print(f"\nTotal de pacientes: {total}")
    return total

# Muestra los diagnósticos más frecuentes (usa Counter).
# Devuelve el Counter.
def reporte_diagnosticos_frecuentes(lista_pacientes, top_n=None):
    diagnosticos = [ (p.get("Diagnostico") or "Sin diagnóstico").strip() for p in lista_pacientes ]
    contador = Counter(diagnosticos)
    mas_comunes = contador.most_common(top_n) if top_n else contador.most_common()
    print("\n=== Diagnósticos más frecuentes ===")
    for diag, cuenta in mas_comunes:
        print(f"{diag}: {cuenta}")
    return contador

# Cuenta pacientes por género (según clave 'Genero').
def reporte_por_genero(lista_pacientes):
    generos = [ (p.get("Genero") or "No especificado").capitalize() for p in lista_pacientes ]
    contador = Counter(generos)
    print("\n=== Pacientes por género ===")
    for gen, cantidad in contador.items():
        print(f"{gen}: {cantidad}")
    return contador

# Filtra > 60.
def reporte_pacientes_mayores_de_60(lista_pacientes):
    # comprobar si al menos uno tiene edad
    tiene_edad = any(('Edad' in p) or ('edad' in p) for p in lista_pacientes)
    if not tiene_edad:
        print("\nNo hay campo 'Edad' en los registros. No es posible generar el reporte de mayores de 60.")
        return []

    mayores = []
    for p in lista_pacientes:
        edad = p.get('Edad') or p.get('edad')
        try:
            if isinstance(edad, (int, float)) and edad > 60:
                mayores.append(p)
        except Exception:
            continue

    print(f"\n=== Pacientes mayores de 60 ({len(mayores)}) ===")
    for p in mayores:
        imprimir_paciente(p)
    return mayores