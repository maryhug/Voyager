# 17 Adivina el número

import random
n_r = random.randint(1, 7)
print("hi, tienes 3 intentos, para ganar esta ruleta rusa. ")
for i in range(3):
    while True:
        try:
            cargador = int(input(" escoje un nomero "))
            if cargador == n_r:
              print("felizidades eres el afortunado. ")
              exit()
            else:
              print("game over")
            break 
        except ValueError:
           print("Ese, no es un nuemro. Mi hermanito. ")
           break
else:
   print(F"Que triste, se perdio uno mas. Bueno el numero era {n_r} ")