# 8 Número positivo, negativo o cero.

# Se pide un número y se determina si es positivo, negativo o cero
numero = int(input("Dime un número: "))
if numero > 0:
    print("Positivo, para covid.")
elif numero < 0:
    print("Negativo.")
else:
    print("Cero")