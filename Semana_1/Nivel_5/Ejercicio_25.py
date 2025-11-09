# Sistema de calificaciones.

print("=== Sistema de Calificaciones ===")

cantidad = input("¿Cuántos estudiantes vas a ingresar?: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Por favor ingresa un número entero positivo: ")

cantidad = int(cantidad)

nombres = []
notas = []

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")

    nombre = input("Nombre del estudiante: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Ingresa de nuevo: ").strip()

    while True:
        nota = input("Ingresa la nota (0 a 5, ejemplo 3.5): ").replace(',', '.').strip()

        if nota.replace('.', '', 1).isdigit():
            nota = float(nota)
            if 0 <= nota <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        else:
            print("Solo se permiten números (por ejemplo: 4.5).")

    nombres.append(nombre)
    notas.append(nota)

promedio = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)

print("\n=== RESULTADOS ===")
print(f"Total de estudiantes: {cantidad}")
print(f"Promedio general: {promedio:.2f}")
print(f"Nota más alta: {nota_max:.2f}")
print(f"Nota más baja: {nota_min:.2f}")

print("\n--- Clasificación ---")
for i in range(cantidad):
    if notas[i] < 3.0:
        estado = "Reprobado"
    elif notas[i] < 5.0:
        estado = "Aprobado"
    else:
        estado = "Excelente"

    print(f"{nombres[i]} - Nota: {notas[i]:.1f} - {estado}")