# 1 hola usuario.
"""
nombre = input("¿cual es tu nombre?. ") # este comonado, le hace una pregunta al usuario, y no deja que se ejecute la siguente linea hasta que respondida la pregunta. esta pregunta se hace para asignarle un valor a la variable
edad = int(input("¿cuantos años tienes?. ")) # hace lo mismo que la primer linea, pero en este caso, pide un numero entero.
print(f"mi nombre es {nombre}, y tengo {edad}") # muestra en pantalla, la respuesta dadas anterior mente 
"""
# 2 Suma de dos números.
"""
numero1 = int(input("dame un numero por favor. "))
numero2 = int(input("dame otro numero por favor. "))
print(numero1*numero2)
"""
# 3 Área del triángulo.
"""
altura = int(input("dime la altura del triangulo. "))
base = int(input("dime las medidas de la base del triangulo. "))
print((altura + base) / 2 )
"""
# 4 Conversor de grados Celsius a Fahrenheit.
"""
celsius = int(input("¿ a que tenmperatura estamos?. "))
fahrenheit = int(celsius * (9 / 5) + 32 )
print(f"la temperatura en fahrenheit es {fahrenheit}.")
"""
# 5 Tipo de dato.
"""
numero = 45
texto = "hola mundo "
print(type(numero))
print(type(texto))
"""
# 6 Edad futura.
"""
edad = int(input("¿cual es tu edad?. "))
print(edad + 10)
"""
# NIVEL 2
# 7 Mayor de edad.
"""
edad = int(input("¿cuantos años tienes?. "))
if edad >= 18:
    print(" ya estas muy viejo.")
else:
    print("eres un sol")
"""
# 8 Número positivo, negativo o cero.
"""
numero = int(input("dime un numero. "))
if numero > 0:
    print("positivo, para covid.")
elif numero < 0:
    print("negativo.")
else:
    print("cero")
"""
# 9 Par o impar.
"""
for i in range (0, 100):
    if i % 2 == 0:
        print(F"par {i}. ")
    else:
        print(F"inpar {i}. ")
"""
# 10 Calculadora básica. 
"""
print("bien benido a calculos s.a.s. ")
print("1. suma. ")
print("2. resta. ")
print("3. division. ")
print("4. multiplicasion. ")
op = int(input("¿que deceas hacer?. "))
e1 = int(input("ingreza un numero. "))
e2 = int(input("ingreza otro numero. "))
if op == 1:
    print(f"la respuesta es {e1 + e2}.")
elif op == 2:
    print(f"la respuesta es {e1 - e2}.")
elif op == 3:
    print(f"la respuesta es {e1/e2}.")
elif op == 4:
    print(f"la respuesta es {e1*e2}.")
"""
# 11 Clasificador de notas
"""
notas = [1, 2, 3, 4, 5,]
nota = int(input("¿que nota sacaste del 1 al 5?. "))
if nota == 1:
    print(" venda bonais. ")
elif nota == 2:
    print("Reprobado. ")
elif nota == 3:
    print("Reprobado. ")
elif nota == 4:
    print("aprobado. ")
elif nota == 5:
    print("Excelente. ")
"""
# 12 Comparador de tres números: mayor y menor
numeros = []
for i in range (3):
    n = int(input("dame un numero po favor. "))
    numeros.append(n)
maximo = max (numeros)
minimo= min(numeros)
print(f" el nimero mayor es {maximo}, y el menor es {minimo}. ")
# 13 