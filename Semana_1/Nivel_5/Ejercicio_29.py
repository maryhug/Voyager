# Calculadora avanzada (usar funciones).

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b
def potencia(a, b):
    return a ** b

def raiz_n(a, n):
    if n == 0:
        return None
    return a ** (1.0 / n)

def factorial(n):
    if n < 0 or int(n) != n:
        return None
    n = int(n)
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def leer_numero(prompt):
    s = input(prompt).replace(',', '.').strip()
    while not (s.replace('.', '', 1).lstrip('-').isdigit() and s.count('.') <= 1):
        s = input("Número inválido. Ingresa de nuevo: ").replace(',', '.').strip()
    return float(s)

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
    if opc == "1":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", sumar(a, b))
    elif opc == "2":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", restar(a, b))
    elif opc == "3":
        a = leer_numero("a = "); b = leer_numero("b = ")
        print("Resultado:", multiplicar(a, b))
    elif opc == "4":
        a = leer_numero("a = "); b = leer_numero("b = ")
        r = dividir(a, b)
        if r is None:
            print("Error: división por cero.")
        else:
            print("Resultado:", r)
    elif opc == "5":
        a = leer_numero("base = "); b = leer_numero("exponente = ")
        print("Resultado:", potencia(a, b))
    elif opc == "6":
        a = leer_numero("Número (>=0 preferible) = "); n = leer_numero("Raíz n = ")
        if n == 0:
            print("Error: raíz n con n=0 no definida.")
        else:
            print("Resultado:", raiz_n(a, n))
    elif opc == "7":
        s = input("n (entero >=0) = ").strip()
        while not (s.isdigit()):
            s = input("Valor inválido. Ingresa un entero >= 0: ").strip()
        n = int(s)
        print("Resultado:", factorial(n))
    elif opc == "8":
        print("Saliendo de la calculadora.")
        break
    else:
        print("Opción inválida.")