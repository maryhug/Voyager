# Sistema de calificación de estudiantes.
# Mensaje de bienvenida
print("Bienvenido al sistema de calificación física.")
print("Basado en un sistema de calificación del 1 al 10.")

# Se solicita el nombre del usuario
nombre = input("Ingrese su nombre: ")

try:
    # Se pide cuántas notas se van a evaluar
    num = int(input("Ingrese el número de notas a evaluar: "))
    
    # Se crean las notas usando comprensión de listas
    notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(num)]
    
    # Se calcula el promedio de las notas
    promedio = sum(notas) / num

    # Se muestran los resultados según el promedio obtenido
    if promedio == 10:
        print(f"Hermano {nombre}, usted es una máquina. Su promedio físico es de {promedio}.")
    elif 8 <= promedio <= 9:
        print(f"Esooo {nombre}, vamos mi compa. Tu actitud física es de {promedio}.")
    elif 6 <= promedio <= 7:
        print(f"Vamos {nombre}, tu actitud física es de {promedio}. Échale ganas mi compa.")
    elif promedio == 5:
        print(f"Mi compa {nombre}, tu actitud física es de {promedio}. Métale al modo guerra mi compa.")
    elif 0 <= promedio < 5:
        print(f"Mi compa {nombre}, usted sacó {promedio} en actitud física. "
              "¿Cómo espera conseguir algo en la vida sin disciplina? Métale al modo guerra mi compa.")
    else:
        print("Error: la nota no está en el rango permitido (0 a 10).")

# Captura de errores si el usuario no ingresa un número válido
except ValueError:
    print("Eso no es un número, mi compa.")