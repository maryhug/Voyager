# Ejercicio 19.
# Lista de frutas.

# Ejercicio 20.
# Agregar y eliminar frutas.

# Ejercicio 21.
# Buscar un elemento en la lista.
frutas = []

def agregar():
    while True:
        try:
            num = int(input("¿Cuántos frutas desea ingresar?: "))
            break
        except ValueError:
            print("Entrada invalida, solo números")
            continue

    for i in range(num):
        agg = input(f"Ingresa fruta {i + 1}: ").lower()
        frutas.append(agg)
    print()

def eliminar():
    if not frutas:
        print("No hay frutas para eliminar")
    else:
        print(f"Frutas disponibles: {frutas}")
        rem = input("Elimina una fruta: ").lower()
        if rem in frutas:
            frutas.remove(rem)
            print(f"Frutas restantes: {frutas}")
        else:
            print("Esa fruta no existe en la lista")
        print()

def listar():
    print("Lista de frutas ingresadas:")
    if frutas:
        print(frutas)
    else:
        print("No hay frutas ingresados")
    print()

def buscar():
    buscar = str(input("\nIngresa la fruta que desea buscar: "))

    if buscar in frutas:
        print(f"La fruta {buscar} esta en la lista")
    else:
        print("No esta la fruta que desea buscar")
    print()

op = 1
while op != 5:
    print("Menú de Frutas")
    print('1. Listar Frutas'
          '\n2. Agregar Fruta'
          '\n3. Eliminar Fruta'
          '\n4. Buscar Fruta'
          '\n5. Salir')
    op = int(input('Ingresa una opción: '))

    print()
    if op == 1:
        listar()
    elif op == 2:
        agregar()
    elif op == 3:
        eliminar()
    elif op == 4:
        buscar()
    elif op == 5:
        print('Salio...')
    else:
        print('Ingrese una opción valida')

# Ejercicio 22.
# Lista de números y promedio.
lista = []
total = 0

num = int(input("Cuantos números desea ingresar: "))
print()
for i in range(num):
    valor = input(f"Ingresa tu numero #{i + 1}: ")
    if valor != "":
        valor = int(valor)
        lista.append(valor)

for n in lista:
    total += n

promedio = total / num
print(f"\nLa suma de estos números {lista} es: {total}"
      f"\nPor lo tanto su promedio es: {promedio}")

# Ejercicio 23.
# Números pares: guardar solo los pares.
# Ejercicio 24.
# Eliminar duplicados.
print()
pares = []
num = int(input("Cuantos números desea ingresar: "))

for i in range(num):
    while True:
        entrada = input(f"Ingresa tu numero #{i + 1}: ")
        try:
            valor = int(entrada)
            break
        except ValueError:
            print("Entrada inválida, ingrese un número entero.")

    if valor % 2 == 0:
        pares.append(valor)
print(pares)

duplicados = input("\nDesea eliminar duplicados (S/N): ").lower()
if duplicados in "S".lower():
    visto = set()
    resultado = []
    for o in pares:
        if o not in visto:
            visto.add(o)
            resultado.append(o)
    print(f"La nueva lista sin duplicados es: {resultado}")
else:
    print("Okey")