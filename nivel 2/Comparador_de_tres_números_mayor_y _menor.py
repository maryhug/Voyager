# 12 Comparador de tres números: mayor y menor

numeros = []
n = int(input("dame un numero po favor. "))
numeros.append(n)
r = int(input("dame un numero po favor. "))
numeros.append(r)
p = int(input("dame un numero po favor. "))
numeros.append(p)
maximo = n
minimo = n
if p > maximo:
    maximo = p
if p < minimo:
    minimo = p
if r < minimo:
    minimo = r
if r > maximo:
    maximo = r
print(f" el nimero mayor es {maximo}, y el menor es {minimo}. ")
