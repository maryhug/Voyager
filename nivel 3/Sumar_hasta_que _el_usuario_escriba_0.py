# 18 Sumar hasta que el usuario escriba 0.

numero = 0
print("Bienvenido, Dios te bendiga ")
print("Escribe números para sumarlos. Si escribes 0, el programa termina.\n")
while True:
    try:
       n = int(input("ue numero deseas que se sume. "))
       if n == 0:
          print("hasta luego")
          break
       else:
          numero += n 
       print(numero) 
    except ValueError:
       print("eso no es un numero")