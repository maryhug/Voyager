#NIVEL 1

#1. Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
"""
nombre = input("Ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

print(f"Hola {nombre}, tienes {edad} años")
"""

#2. Suma de dos números.
"""
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))

suma = n1 + n2

print(f"La suma de los números es: {suma}")
"""

#3. Área del triángulo.
"""
b = float(input("Ingrese el valor de la base del triángulo (cm): "))
h = float(input("Ingrese el valor de la altura del triángulo (cm) "))

area = b * h / 2

print(f"El área del triángulo es: {area}")
"""

#4. Conversor de grados Celsius a Fahrenheit.
"""
c = float(input("Ingrese los grados Celsius para convertirlos a Farentheit: "))

f = c * (9/5) + 32

print(f"{c}° Celsius son {f}° Farentheit")
"""

#5. Tipo de dato: usar type() para mostrar el tipo de cada variable.
"""
dato = input("Ingrese algo para ver qué de tipo de dato es: ")

try:
    dato = int(dato)
except ValueError:
    try:
        dato = float(dato)
    except ValueError:
        if dato.lower() in ['true','false']:
                dato = bool(dato.lower() == 'true')

print("Ingresaste un dato de tipo: ",type(dato))
"""

#6. Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
"""
edad = int(input("Ingrese su edad: "))

age = edad + 10
print(f"Dentro de 10 años tendrás {age} años.")
"""

#NIVEL 2

#7. Mayor de edad.
"""
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
"""

#8.Número positivo, negativo o cero.
"""
num = float(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else: 
    print("El número es igual a cero.")
"""

#9. Par o impar.
"""
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("El número es par.")
else: 
    print("EL número es impar.")
"""

#10. Calculadora básica con +, -, *, /.
"""
print("Calculadora")
print("\n1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("\n¿Qué desea realizar?: "))

n1 = float(input("Digite el primer número: "))
n2 = float(input("Digite el segundo número: "))

if opcion == 1:
  resultado = n1 + n2
elif opcion == 2:
  resultado = n1 - n2
elif opcion == 3:
  resultado = n1 * n2
else: 
  resultado = n1 / n2

print(f"El resultado es: {resultado}")
"""

#11. Clasificador de notas (Excelente, Aprobado, Reprobado).
"""
nota = float(input("Digite su nota: "))

if nota < 3.0:
    print("Ha reprobado.")
elif (nota >= 3.0)and(nota <= 4.9):
    print("Ha aprobado.")
else:
    print("Calificación perfecta, excelente.")
"""

#12. Comparador de tres números: mayor y menor.
"""
numeros = []

for i in range(3):
    num = int(input("Digite un número: "))
    numeros.append(num)

max = max(numeros)
min = min(numeros)

print("\nEl número mayor es:", max)
print("El número menor es:", min)
"""

#NIVEL 3

#13. Contar del 1 al 10.
"""
for i in range(10):
    print(i+1)
"""

#14. Sumatoria del 1 al n.
"""
n = int(input("Digite hasta qué número quiere hacer la sumatoria: "))
suma = 0

for i in range(1, n + 1):
    suma = suma + i
print(f"La sumatoria es: {suma}")
"""

#15. Tabla de multiplicar.
"""
num = int(input("Digite un número para ver su tabla de multiplicar: "))

for i in range(1, 10 + 1):
    mul = num * i
    print(f"{num} * {i} = {mul}")
"""

#16. Contador regresivo con while.
"""
num = int(input("Digite un número para hacer una cuenta regresiva: "))
          
while num >= 0:
    print(num)
    num = num - 1
"""

#17. Adivina el número (usar random).
"""
import random

num_random = random.randint(1, 100)

print("Adivina el número del 1 al 100")

intento = 0
adivinado = False

while not adivinado:
    intento = intento + 1
    num = int(input("\nDigite un número: "))

    if num > num_random:
        print("El número que ingresaste es mayor.")
    elif num < num_random:
        print("El número que ingresaste es menor.")
    else:
        print(f"Adivinaste el número {num_random}! En {intento} intentos.")
        adivinado = True
"""

#18. Sumar hasta que el usuario escriba 0.
"""
num = int(input("Digite un número: "))
suma = 0

while num != 0:
    suma = suma + num
    print(f"La resultado es: {suma}")
    num = int(input("Digite otro número (0 para terminar): "))

print(f"El resultado final es: {suma}")
"""

#NIVEL 4

#19. Lista de frutas.
"""
frutas = ["Manzana", "Pera", "Mango", "Uva", "Durazno"]

print(frutas)
"""

#20. Agregar y eliminar frutas.
"""
frutas = ["manzana", "pera", "mango", "uva", "durazno"]

print(frutas)

while True:
    agg = input("\nDesea agregar alguna fruta a la lista? (si/no): ")
    
    if agg.lower() == 'si':
        fruta = input("Digite la fruta que desea agregar: ")
        frutas.append(fruta.lower())
        print(frutas)

    elif agg.lower() == 'no':

        rem = input("\nDesea eliminar alguna fruta de la lista? (si/no): ")

        if rem.lower() == 'si':
            fruta = input("Digite la fruta que desea eliminar: ")

            if fruta.lower() in frutas:
                frutas.remove(fruta.lower())
                print("Fruta eliminada: ", frutas)
            else: 
                print("Esta fruta no está en la lista.")

        elif rem.lower() == 'no':
            print("\nPrograma finalizado, así quedó la lista: ", frutas)
            break
        else:
            print("La respuesta ingresada no es válida.")
            break
    else:
        print("La respuesta ingresada no es válida.")
"""

#21. Buscar un elemento en la lista.
"""
trasnporte = ['carro', 'moto', 'bicicleta', 'patineta', 'avión', 'barco', 'tren', 'bus']

print(trasnporte)
buscar = input("\nDigite el elemento que quiere buscar: ")

try:
    i = trasnporte.index(buscar.lower())
    print(f"El elemento {buscar} está en la posición ", i + 1)

except ValueError:
    print(f"El elemento {buscar} no se encuentra en la lista.")
"""

#22. Lista de números y promedio.
"""
numeros = []

num = int(input("Ingrese un número: "))
suma = 0
i = 0

while num != 0:

    numeros.append(num)
    suma = suma + num
    i = i + 1
    num = int(input("Ingrese otro número (0 para terminar y calcular el promedio): "))

promedio = suma / i

print(numeros)
print(f"El promedio es: {promedio}")
"""

#23. Números pares: guardar solo los pares.
"""
numeros = []

num = int(input("Ingrese un número: "))

while num != 0:
    if num % 2 == 0:
        numeros.append(num)
    num = int(input("Ingrese otro número (0 para terminar y mostrar la lista): "))

print(numeros)
"""

#24. Eliminar duplicados.
"""
numeros = []

num = int(input("Ingrese un número: "))

while num != 0:
    numeros.append(num)
    num = int(input("Ingrese otro número (0 para terminar): "))

print(f"\nEsta es la lista original: {numeros}")

sin_dup = []

for i in numeros:
    if i not in sin_dup:
        sin_dup.append(i)

print(f"\nEsta es la lista sin duplicados: {sin_dup}")
"""

#NIVEL 5

#25. Sistema de calificaciones.
"""
print ("Sistema de calificaciones: ")

talleres = []
examenes = []
parciales = []

cont_t = 0
cont_e = 0
cont_p = 0

opcion = 0

while opcion != 4:
    print("\nMenú:")
    print("\n1. Agregar una nota")
    print("2. Mostrar notas actuales")
    print("3. Calcular promedio final")
    print("4. Salir")

    opcion = int(input("\n¿Qué desea hacer?: "))

    if opcion == 1:

        print("\nTipo de nota:")
        print("\n1. Taller (4 del 5% c/u)")
        print("2. Exámen (3 del 10% c/u)")
        print("3. Parcial (2 del 25% c/u)")
        tipo = int(input("\n¿Qué nota desea agregar?: "))

        if tipo == 1:

            while cont_t < 4:
                nota = float(input("\nDigite la nota del taller: "))
                talleres.append(nota)
                cont_t = cont_t + 1
                print("Nota agregada correctamente.")
            
        elif tipo == 2:

            while cont_e < 3:
                nota = float(input("\nDigite la nota del exámen: "))
                examenes.append(nota)
                cont_e = cont_e + 1
                print("Nota agregada correctamente.")

        elif tipo == 3:

            while cont_p < 2:
                nota = float(input("\nDigite la nota del parcial: "))
                parciales.append(nota)
                cont_p = cont_p + 1
                print("Nota agregada correctamente.")         
            
        else:
            print("\nDigite un valor válido.")

    elif opcion == 2:

        print("\nNotas actuales: ")

        if cont_t == 0:
            print("\nNo hay notas de talleres.")
        else: 
            print(f"\nTalleres: {talleres}")

        if cont_e == 0:
            print("No hay notas de exámenes.")
        else:
            print(f"Exámenes: {examenes}")

        if cont_p == 0:
            print("No hay notas de parciales.")
        else:
            print(f"Parciales: {parciales}")

    elif opcion == 3:

        if cont_t == 4:
            prom_t = (talleres[0] + talleres[1] + talleres[2] + talleres[3])/4
            print(f"\nPromedio de los talleres: {prom_t}")
        else:
            print("\nNo se puede calcular el promedio de los talleres porque no hay notas.")
        
        if cont_e == 3:
            prom_e = (examenes[0] + examenes[1] + examenes[2])/3
            print(f"Promedio de los exámenes: {prom_e}")
        else:
            print("No se puede calcular el promedio de los exámenes porque no hay notas.")
        
        if cont_p == 2:
            prom_p = (parciales[0] + parciales[1])/2
            print(f"Promedio de los parciales: {prom_p}")
        else:
            print("No se puede calcular el promedio de los parciales porque no hay notas.")  

        if (cont_t == 4) and (cont_e == 3) and (cont_p == 2):
            nota_final = (prom_t * 0.05 * 4 + prom_e * 0.10 * 3 + prom_p * 0.25 * 2)
            print(f"\nNota final: {nota_final}")

            if nota_final >= 3:
                print("Ha aprobado, felicidades!")
            else:
                print("Ha reprobado, estudie.")
        else:
            print("\nNo se puede calcular la nota final porque faltan notas.") 

    elif opcion == 4:
        print("\nHasta pronto.")
"""

#26. Carrito de compras.


