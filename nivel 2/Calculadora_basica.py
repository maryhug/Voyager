# 10 Calculadora básica. 

# Se muestra el menú de operaciones disponibles
print("Bienvenido a cálculos S.A.S.")
print("1. Suma.")
print("2. Resta.")
print("3. División.")
print("4. Multiplicación.")

# Se pide al usuario la operación que desea realizar
op = int(input("¿Qué deseas hacer? "))

# Se piden los dos números a operar
e1 = int(input("Ingresa un número: "))
e2 = int(input("Ingresa otro número: "))

try:
    # Se ejecuta la operación elegida
    if op == 1:
        print(f"La respuesta es {e1 + e2}.")
    elif op == 2:
        print(f"La respuesta es {e1 - e2}.")
    elif op == 3:
        print(f"La respuesta es {e1 / e2}.")
    elif op == 4:
        print(f"La respuesta es {e1 * e2}.")
    else:
        print("Operación no válida.")
except ZeroDivisionError:
    # Este bloque se ejecuta si el usuario intenta dividir entre 0
    print("Error: no se puede dividir entre cero.")
