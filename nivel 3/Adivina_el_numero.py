# 17 Adivina el número

import random
n_r = random.randint(1, 7)  # Se genera un número aleatorio entre 1 y 7
print("Hi, tienes 3 intentos, para ganar esta ruleta rusa. ")
for i in range(3):
    while True:
        try:
            cargador = int(input("Escoge un número: "))
            if cargador == n_r:
                print("Felicidades, eres el afortunado.")  # Si acierta, termina el programa
                exit()
            else:
                print("Game over")  # Si falla, continúa
            break
        except ValueError:
            print("Eso no es un número. Mi hermanito.")  # Controla entradas inválidas
            break
else:
    print(f"Qué triste, se perdió uno más. Bueno, el número era {n_r}")
