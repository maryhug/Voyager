# Mayor de edad.
age = int(input("\n¿Cuantos años tienes?: "))
if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Número positivo, negativo o cero.
num = int(input("\nIngresa un número: "))
if num == 0:
    print("Tu numero es 0")
elif num > 0:
    print("Tu numero es positivo")
else:
    print("Tu numero es negativo")

# Par o impar.
num = int(input("\nIngresa un número: "))
if num % 2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es impar")

# Calculadora básica con +, -, *, /.
while True:

    print("\nCalculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Division")
    print("5. Salir")

    try:
        opc = int(input("¿Que desea realizar?: "))
        if opc != 5:
            num1 = int(input("Ingresa el primer numero:"))
            num2 = int(input("Ingresa el segundo numero:"))
    except ValueError:
        print("Opción invalida")
        continue

    if opc == 1:
        num3 = num1 + num2
        print("El resultado es de la suma es: ", num3)
    elif opc == 2:
        num3 = num1 - num2
        print("El resultado es de la resta es: ", num3)
    elif opc == 3:
        num3 = num1 * num2
        print("El resultado es de la multiplicación es: ", num3)
    elif opc == 4:
        if num2 == 0:
            print("División invalida")
            continue
        num3 = num1 / num2
        print("El resultado es de la división es: ", num3)
    elif opc == 5:
        print("Byee!!")
        break
    else:
        print("\nOpción invalida")
    print("=" * 50)

# Clasificador de notas (Excelente, Aprobado, Reprobado).
while True:
    try:
        note = float(input("\nIngresa tu nota: "))
        if 0 <= note < 2.9:
            print("Reprobado")
        elif 3.0 <= note < 4.9:
            print("Aprobado")
        elif note >= 5.0:
            print("Excelente")
        else:
            print("La nota no puede ser negativa.")
        break
    except ValueError:
        print("Solo se permiten números decimales (por ejemplo: 3.5). Intenta de nuevo.")

# Mayor y menor de 3 números
print()
lista = []

for i in range(3):
    num = int(input(f"Ingresa {i + 1} números: "))
    lista.append(num)
    print(lista)

maximo = max(lista)
minimo = min(lista)
print("Tu numero max", maximo)
print("Tu numero min", minimo)
