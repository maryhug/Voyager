# 10 Calculadora básica. 

print("bien benido a calculos s.a.s. ")
print("1. suma. ")
print("2. resta. ")
print("3. division. ")
print("4. multiplicasion. ")
op = int(input("¿que deceas hacer?. "))
e1 = int(input("ingreza un numero. "))
e2 = int(input("ingreza otro numero. "))
try:
    if op == 1:
        print(f"la respuesta es {e1 + e2}.")
    elif op == 2:
        print(f"la respuesta es {e1 - e2}.")
    elif op == 3:
        print(f"la respuesta es {e1/e2}.")
    elif op == 4:
        print(f"la respuesta es {e1*e2}.")
    else:
        print("operacion no valida.")
except ZeroDivisionError:
    print("error.")