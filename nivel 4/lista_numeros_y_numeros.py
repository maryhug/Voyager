# 22 Lista de numeros y promedio.
print(" Bienvenido, Dios te bendiga. ")

# Se pide cuántos números se van a ingresar
n = int(input(" ¿De cuántos números va a ser el promedio? "))

suma = 0  # Acumula la suma de los números
total = []  # Guarda todos los números ingresados

# Se usa un bucle for normal para poder pedir números uno por uno
for i in range(n):
    dupla = float(input(f"Dime el número {i + 1}: "))  # Pide el número
    total.append(dupla)  # Lo agrega a la lista
    suma += dupla  # Lo suma al total

# Se calcula el promedio
R = suma / n

# Se muestra el resultado final
print(f" El promedio de los números {total} es {R}. ")
    