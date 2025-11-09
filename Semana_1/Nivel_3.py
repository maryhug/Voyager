# Ejercicio 13.
# Contar del 1 al 10.
for i in range(10):
    print(i + 1)

# Ejercicio 14.
# Sumatoria del 1 al n.
while True:
    try:
        final = int(input("Hasta qué número quiere sumar (entero positivo): "))
        if final < 1:
            print("Ingrese un entero mayor o igual a 1.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")

total = final * (final + 1) // 2
print(f"La suma de 1 a {final} es: {total}")

# Ejercicio 15.
# Tabla de multiplicar.
hasta = 10
while True:
    try:
        multi = int(input("\n¿Qué tabla de multiplicar quiere?: "))
        break
    except ValueError:
        print("Solo números, no letras ni nada raro. Intente de nuevo.")

print(f"\nTabla de multiplicar del {multi} (hasta {hasta}):")
for i in range(1, hasta + 1):
    print(f"{multi} x {i} = {multi * i}")

# Ejercicio 16.
# Contador regresivo con while.
reg = int(input("\n¿Hasta que número quiere que se haga la regresión?: "))
for i in range(reg, 0, -1):
    print(f"- {i}")

# Ejercicio 17.
# Adivina el número (usar random).
import random

print("\nIngresarás el rango de números que quieres adivinar.")
print("Por ejemplo, si ingresas mínimo (6) y máximo (9), el número a adivinar estará entre esos números.")

minimo = int(input("¿Cuál es el número mínimo? "))
maximo = int(input("¿Cuál es el número máximo? "))

numero_secreto = random.randint(minimo, maximo)
intentos = 5

for i in range(intentos):
    adivina = int(input(f"\nIntento {i + 1}/{intentos} - Adivina el número (entre {minimo} y {maximo}): "))

    if adivina == numero_secreto:
        print("¡Adivinaste el número!")
        break
    else:
        if adivina < numero_secreto:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")

if adivina != numero_secreto:
    print(f"\nNo adivinaste. El número secreto era {numero_secreto}.")

# Ejercicio 18.
# Sumar hasta que el usuario escriba 0.
sumador = 0
bandera = True
print("\nSuma acumulativa: introduce números y escribe 0 para terminar.")
while bandera:
    entrada = input("Introduce un número (0 para terminar): ").strip()
    try:
        num = int(entrada)
    except ValueError:
        print("Entrada inválida. Introduce un número entero.")
        continue
    if num == 0:
        bandera = False
        break
    sumador += num
    print(f"Suma parcial: {sumador}")
print(f"Suma total: {sumador}")
