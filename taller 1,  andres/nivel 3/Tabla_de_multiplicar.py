# 15 Tabla de multiplicar.
# Se pide al usuario el número del cual quiere la tabla
n = int(input("Hola, bienvenido a tablas.comm, dime de ¿cuál número quieres una tabla? "))
# Se recorre del 1 al 10 multiplicando y mostrando los resultados
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")