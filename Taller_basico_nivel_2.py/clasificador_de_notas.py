notas = int(input("Ingrese la nota del estudiante (0-100): "))

if 90 <= notas <= 100:
    print("excelente")
elif 70 <= notas < 90:
    print("aprobado")
elif 0 <= notas < 70:
    print("reprobado")
else:
    print("Nota fuera de rango")
