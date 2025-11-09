# Sistema de calificaciones.
print("=== Sistema de Calificaciones ===")

# Solicita al usuario cuántos estudiantes ingresará
cantidad = input("¿Cuántos estudiantes vas a ingresar?: ")

# Válida que la entrada sea un número entero positivo
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Por favor ingresa un número entero positivo: ")

# Convierte la cantidad un número entero
cantidad = int(cantidad)

# Crea dos listas vacías para almacenar los datos de cada estudiante
nombres = []
notas = []

# Recorre desde 0 hasta la cantidad de estudiantes ingresada
for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")

    # Valida que el nombre no esté vacío
    nombre = input("Nombre del estudiante: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Ingresa de nuevo: ").strip()

    # Ciclo infinito que solo se rompe cuando se ingresa una nota válida
    while True:
        # Solicita la nota y reemplaza comas por puntos para aceptar ambos formatos (3,5 o 3.5)
        nota = input("Ingresa la nota (0 a 5, ejemplo 3.5): ").replace(',', '.').strip()

        # Verifica si la entrada es un número decimal válido
        # replace('.', '', 1): elimina el primer punto para verificar si el resto son dígitos
        # El parámetro 1 asegura eliminar solo un punto (evita casos como 3.4.5)
        if nota.replace('.', '', 1).isdigit():
            # Convierte el texto a número decimal (float)
            nota = float(nota)
            # Verifica que la nota esté en el rango permitido (0 a 5)
            if 0 <= nota <= 5:
                break   # Sale del ciclo while si la nota es válida
            else:
                print("La nota debe estar entre 0 y 5.")
        else:
            print("Solo se permiten números (por ejemplo: 4.5).")

    # Agrega el nombre y la nota validados a sus respectivas listas
    nombres.append(nombre)
    notas.append(nota)

# promedio: resultado de dividir la suma total entre la cantidad de notas
promedio = sum(notas) / len(notas)
# Encuentra el valor más alto en la lista de notas
nota_max = max(notas)
# Encuentra el valor más bajo en la lista de notas
nota_min = min(notas)

print("\n=== RESULTADOS ===")
print(f"Total de estudiantes: {cantidad}")
# :.2f formatea el número con 2 decimales (ejemplo: 3.75)
print(f"Promedio general: {promedio:.2f}")
print(f"Nota más alta: {nota_max:.2f}")
print(f"Nota más baja: {nota_min:.2f}")

print("\n--- Clasificación ---")
# Recorre cada estudiante para clasificarlo según su nota
for i in range(cantidad):
    if notas[i] < 3.0:
        estado = "Reprobado"
    elif notas[i] < 5.0:
        estado = "Aprobado"
    else:
        estado = "Excelente"
    # Imprime el resultado individual de cada estudiante
    print(f"{nombres[i]} - Nota: {notas[i]:.1f} - {estado}")