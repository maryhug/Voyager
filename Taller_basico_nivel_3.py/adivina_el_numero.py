import random 

numero_secreto = random.randint(1,10)
intento = 0

print("adivina el numero entre el 1 y el 10")

while True:
 intento = int(input("tu intento: "))

 if intento < numero_secreto:
  print("mas alto")
 elif intento > numero_secreto:
  print("mas bajo")
 else: 
   print("GANASTE")
 