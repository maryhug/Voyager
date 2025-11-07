numero = (83, 27, 65, 42, 91, 10, 57)
def comparar_numeros(num1, num2, num3, num4, num5, num6, num7):
    mayor = max(num1, num2, num3, num4, num5, num6, num7)
    menor = min(num1, num2, num3, num4, num5, num6, num7)
    return mayor, menor
print("el numero mayor es:", comparar_numeros(*numero)[0])
print("el numero menor es:", comparar_numeros(*numero)[1])