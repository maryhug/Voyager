# Modulo para ingresar pacientes
# Autor: [ Jhon Stiven Zuluaga Jaramillo. ]

import uuid # importa, a nuestro archivo .py, la herramienta uuid.
import re   # impotar, a nuestro archivo .py, la herramienta re.

# lista, en la que se van a guardar los pacientes.
  
pacientes = []

# Funcion, que pregunta numero entero y lo valida.

def perdir_numero_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("El número debe ser mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Ingresa un número válido.")
            
# Funcion, que pregunta y valida textos cortos como nombres.

def pedir_texto(pregunta):
    caracteres = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\'\-]+$")
    while True:
        texto = input(pregunta).strip()
        if texto == "":
            print("Eso no parece un nombre válido.")
            continue
        if caracteres.fullmatch(texto):
            texto = " ".join(texto.split())
            texto = texto.title()
            return texto
        else:
            print(" Eso no parece un nombre válido. Usa solo letras o espacios.")
            
# Funcion, que pregunta y valida. lo que ingresas, sea una de las dos opciones.

def pedir_genero():
    while True:
        genero = input("¿Es Masculino o Femenino? m / f ").strip().lower()
        if genero in ("masculino", "femenino", "m", "f"):
            return genero.capitalize()
        else:
            print(" Debes escribir 'masculino' - 'femenino'. m/f . ")

# Funcion, que pregunta y valida, mucho texto como: un diagnostico.

def pedir_texto_largo(pregunta):
    caracteres = re.compile(r"^[0-9A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\'\-]+$")
    while True:
        mucho_texto = input(pregunta).strip()
        if mucho_texto == "":
            print(" Tienes que poner algo. ")
            continue
        if caracteres.fullmatch(mucho_texto):
            mucho_texto = " ".join(mucho_texto.split())
            return mucho_texto
        else:
            print(" Ingresa un texto válido.")
            
# En esta funcion, se integran, todas las anteriores funciones, para pregunta e ingrezar, 
# los datos del pasiente, a un diccionario y luego este mismo, a una lista. 

def ingresar_paciente():
    ID = int(str(uuid.uuid4().int)[:3])  # Genera un ID de diez números.
    nombre_completo = pedir_texto(" Ingresa el nombre completo del paciente: ").capitalize()
    genero = pedir_genero()
    diagnostico = pedir_texto_largo(" ¿Cuál es el diagnóstico del paciente?: ").capitalize()
    historial = pedir_texto_largo(" ¿Cuál es el historial del paciente?: ").capitalize()
    edad = perdir_numero_entero(" Ingresa la edad del paciente: ")
    
# Combierte, el historial, del diccionario en una lista.
 
    historial = [historial] if historial else []

    diccionario = {
        "ID": ID,
        "Nombre_completo": nombre_completo,
        "Genero": genero,
        "Diagnostico": diagnostico,
        "Historial": historial,
        "Edad": edad
    }
# Guarda los diccionarios, en una lista. 
  
    pacientes.append(diccionario)
    print("Paciente ingresado correctamente:")
    print(f"   ID: {ID} | Nombre: {nombre_completo} | Género: {genero} | "
          f"Diagnóstico: {diagnostico} | Historial: {historial} | Edad: {edad}")