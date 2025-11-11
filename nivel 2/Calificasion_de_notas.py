# 11 Clasificador de notas

# Lista de referencia de notas (no se usa directamente, pero indica el rango)
notas = [1, 2, 3, 4, 5]

# Se pide al usuario su nota y se muestra un mensaje según el valor
nota = int(input("¿Qué nota sacaste del 1 al 5? "))

if nota == 1:
    print("Venda Bonais.")
elif nota == 2:
    print("Reprobado.")
elif nota == 3:
    print("Reprobado.")
elif nota == 4:
    print("Aprobado.")
elif nota == 5:
    print("Excelente.")
else:
    print("Esa nota no existe, mi compaaa.")
