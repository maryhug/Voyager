n = int(input("¿hasta que numero desea sumar?:"))
suma = 0
for i in range(1, n + 1):
    suma += i
print("la sumatoria del 1 al", n, "es:", suma)