#Fundamentos y Variables

# Ejercicio 1.
# Hola usuario: pide al usuario su nombre y edad.
print("Hola usuario!!!")
name = str(input("¿Cual es tu nombre?: "))
age = int(input("¿Cuantos años tienes?: "))
print(f"Hola {name}, tienes {age} años.")

# Ejercicio 2.
# Suma de dos números.
print("\nSumaremos dos números, ingresalos")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
add = num1 + num2
print("El resultado de la operacion es: ", add)

# Ejercicio 3.
# Área del triángulo.
# (Área = base × altura / 2)
print("\nHallaremos el area de un triangulo, ingresa los datos.")
base = float(input("Base: "))
altura = float(input("Altura: "))
area = (base * altura) / 2
print("El area del triangulo es: ", area)

# Ejercicio 4.
# Conversor de grados Celsius a Fahrenheit.
print("\nConvertiremos grados Celsius a Fahrenheit")
celsius = float(input("¿Que °Celsius quiere convertir? "))
transformed = celsius * 1.8 + 32
print("La conversion de Celsius a Fahrenheit es: ", transformed)

# Ejercicio 5.
# Tipo de dato: usar type() para mostrar el tipo de cada variable.
print("\nTipo de dato de cada variable")
print(type(32))
print(type(True))
print(type(9.5))
print(type("Hola mundo!!"))
animales = ["Perro", "Gato", "Elefante", "León", "Delfín"]
print(type(animales))

# Ejercicio 6.
# Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
age = int(input("\n¿Cuantos años tienes?: "))
future = age + 10
print("Tu edad futura en 10 años es: ", future)