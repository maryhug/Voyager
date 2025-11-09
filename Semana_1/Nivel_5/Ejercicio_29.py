# Calculadora avanzada (usar funciones).

# Función que realiza la suma de dos números
def sumar(a, b):
    return a + b

# Función que realiza la resta de dos números
def restar(a, b):
    return a - b

# Función que realiza la multiplicación de dos números
def multiplicar(a, b):
    return a * b

# Función que realiza la división de dos números
def dividir(a, b):
    # Evitar división por cero
    if b == 0:
        return None
    return a / b

# Función que realiza la potencia
def potencia(a, b):
    return a ** b

# Función que realiza la raiz
def raiz_n(a, n):
    # Raíz con índice 0 no está definida
    if n == 0:
        return None
    return a ** (1.0 / n)

# Función que realiza el factorial de dos números
def factorial(n):
    # Validar que n no sea negativo y que sea un número entero
    if n < 0 or int(n) != n:
        return None
    n = int(n)
    # Caso base: 0! = 1
    if n == 0:
        return 1
    # Calcular factorial mediante multiplicación iterativa
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# Solicita y valida un número al usuario.
def leer_numero(prompt):
    s = input(prompt).replace(',', '.').strip()
    # Validar formato numérico (permite negativos con lstrip('-'))
    while not (s.replace('.', '', 1).lstrip('-').isdigit() and s.count('.') <= 1):
        s = input("Número inválido. Ingresa de nuevo: ").replace(',', '.').strip()
    return float(s)

# Muestra el menú principal de la calculadora.
def menu():
    print("\n=== Calculadora avanzada ===")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Potencia")
    print("6) Raíz n-ésima")
    print("7) Factorial (n entero >= 0)")
    print("8) Salir")

while True:
    menu()
    opc = input("Elige opción: ").strip()

    # Opción 1: Suma de dos números
    if opc == "1":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", sumar(a, b))

    # Opción 2: Resta de dos números
    elif opc == "2":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", restar(a, b))

    # Opción 3: Multiplicación de dos números
    elif opc == "3":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", multiplicar(a, b))

    # Opción 4: División de dos números con manejo de división por cero
    elif opc == "4":
        a = leer_numero("a = "); b = leer_numero("b = ")
        r = dividir(a, b)
        # Verificar si la división retornó None (división por cero)
        if r is None:
            print("Error: división por cero.")
        else:
            print("Resultado:", r)

    # Opción 5: Potencia (a^b)
    elif opc == "5":
        a = leer_numero("base = "); b = leer_numero("exponente = ")
        print("Resultado:", potencia(a, b))

    # Opción 6: Raíz n-ésima con validación de n != 0
    elif opc == "6":
        a = leer_numero("Número (>=0 preferible) = "); n = leer_numero("Raíz n = ")
        # Validar que n no sea cero
        if n == 0:
            print("Error: raíz n con n=0 no definida.")
        else:
            print("Resultado:", raiz_n(a, n))

    # Opción 7: Factorial con validación de entero positivo
    elif opc == "7":
        # Solicitar número con validación específica para enteros
        s = input("n (entero >=0) = ").strip()
        # Validar que sea un entero no negativo
        while not (s.isdigit()):
            s = input("Valor inválido. Ingresa un entero >= 0: ").strip()
        n = int(s)
        print("Resultado:", factorial(n))

    # Opción 8: Salir del programa
    elif opc == "8":
        print("Saliendo de la calculadora.")
        break
    # Opción inválida
    else:
        print("Opción inválida.")