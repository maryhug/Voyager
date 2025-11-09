# 15 Tabla de multiplicar.
n = int(input("hola, bienvenido a tablas.comm, dime de ¿cual numero quieres una tabla?. "))
for i in  range(1,11):
    resultado = int(n * i)
    print(f"{n} x {i} = {resultado}")