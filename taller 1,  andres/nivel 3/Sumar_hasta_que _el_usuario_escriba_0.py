# 18 Sumar hasta que el usuario escriba 0.
numero = 0  # Variable que acumula la suma total
print("Bienvenido, Dios te bendiga ")
print("Escribe números para sumarlos. Si escribes 0, el programa termina.\n")
while True:
    try:
        n = int(input("¿Qué número deseas que se sume? "))
        if n == 0:
            print("Hasta luego")
            break  # Sale del bucle si el usuario escribe 0
        else:
            numero += n  # Se suma el número ingresado
        print(f"Suma actual: {numero}")  # Muestra la suma acumulada
    except ValueError:
        print("Eso no es un número")  # Controla entradas inválidas
