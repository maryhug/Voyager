# 9 Par o  inpar.
# 0 al 99, pares e impares
# Se recorre del 0 al 99 y se imprime si el número es par o impar
for i in range(0, 100):
    if i % 2 == 0:
        print(f"Par {i}")
    else:
        print(f"Impar {i}")