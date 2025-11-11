# 14 Sumatoria del 1 al n.
# Se pide hasta qué número se quiere sumar
n = int(input("Bienvenido, Dios te bendiga, hasta qué número deseas que se sume. "))
suma = 0  # Variable para acumular la suma
for i in range(1, n + 1):
    suma += i  # Se va sumando cada número
print(f"La suma total es: {suma}")