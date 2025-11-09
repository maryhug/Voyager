# Calculadora avanzada
import math  # Se importa la librería math para usar funciones matemáticas como sqrt()

# Función para sumar dos números
def suma(a, t):
    return a + t

# Función para restar dos números
def restar(a, t):
    return a - t

# Función para dividir dos números, validando que el divisor no sea cero
def dividir(a, t):
    if t == 0:
        return "no se puede proceder con 0 bro "
    return a / t

# Función para multiplicar dos números
def multiplicar(a, t):
    return a * t

# Función para elevar un número a la potencia de otro
def potencia(a, t):
    return a ** t

# Función para calcular la raíz cuadrada, validando que no sea un número negativo
def raiz(a):
    if a < 0:
        return "no, no no broo"
    return math.sqrt(a)

# Bucle principal del programa
while True:
    # Muestra el menú principal
    print("bienvenido a la calculadora avanzada s.a.s. ")
    print("1. suma. ")
    print("2. resta. ")        
    print("3. división. ")
    print("4. multiplicación. ")
    print("5. potencia. ")
    print("6. raíz cuadrada. ")
    print("7. salir. ")
    try:
        # Solicita al usuario qué desea hacer
        co = int(input(" ¿Qué deseas hacer?. "))
    
        # Opción 1: suma
        if co == 1:
            e1 = float(input(" ingresa el primer número: "))
            e2 = float(input(" ingresa el segundo número: "))
            print(f" la respuesta es {suma(e1, e2)}. ")
            
        # Opción 2: resta
        elif co == 2:
            e1 = float(input(" ingresa el primer número: "))
            e2 = float(input(" ingresa el segundo número: "))         
            print(f" la respuesta es {restar(e1, e2)}. ")    
               
        # Opción 3: división
        elif co == 3:
            e1 = float(input(" ingresa el primer número: "))
            e2 = float(input(" ingresa el segundo número: "))
            print(f" la respuesta es {dividir(e1, e2)}. ")  
            
        # Opción 4: multiplicación
        elif co == 4:
            e1 = float(input(" ingresa el primer número: "))
            e2 = float(input(" ingresa el segundo número: "))
            print(f" la respuesta es {multiplicar(e1, e2)}. ")  
            
        # Opción 5: potencia
        elif co == 5:
            e1 = float(input(" ingresa el primer número: "))
            e2 = float(input(" ingresa el segundo número: "))
            print(f" la respuesta es {potencia(e1, e2)}. ") 
            
        # Opción 6: raíz cuadrada
        elif co == 6:
            e1 = float(input(" ingresa el primer número: "))
            print(f" la respuesta es {raiz(e1)}. ")
            
        # Opción 7: salir del programa
        elif co == 7:
            print("gracias por usar la calculadora avanzada s.a.s. ")
            break   
        
        # Si se ingresa una opción no válida
        else:
            print(" eso no es un número my brooo. ")

    # Controla errores cuando el usuario no ingresa un número
    except ValueError:
        print(" mi compaaaaa puro modo guerraa, pero duerma porque ya ni sabe qué es un número.. ")