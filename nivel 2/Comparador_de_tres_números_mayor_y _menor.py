# 12 Comparador de tres números: mayor y menor
# Se crea una lista vacía para guardar los tres números
numeros = []

# Se piden tres números al usuario y se agregan a la lista
n = int(input("Dame un número por favor: "))
numeros.append(n)
r = int(input("Dame un número por favor: "))
numeros.append(r)
p = int(input("Dame un número por favor: "))
numeros.append(p)

# Se inicializan las variables máximo y mínimo con el primer número
maximo = n
minimo = n

# Se compara el tercer número con los valores actuales de máximo y mínimo
if p > maximo:
    maximo = p
if p < minimo:
    minimo = p

# Se compara el segundo número con los valores actuales de máximo y mínimo
if r < minimo:
    minimo = r
if r > maximo:
    maximo = r

# Se muestra el resultado final
print(f"El número mayor es {maximo}, y el menor es {minimo}.")

