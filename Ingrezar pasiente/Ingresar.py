import uuid # importa, a nuestro archivo .py, la herramienta uuid.
import re
pacientes =[] # lista, en la que se van a guardar los pacientes.  
# Funcion, que pregunta numero entero y lo valida. 
def perdir_numero_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print(" Es no me sirve. ")
            else:
                return valor
        except ValueError:
            print(" Eso no es, un numero, haga el trabajo bien.")
# Funcion, que pregunta y valida textos cortos como nombres.
def pedir_texto(pregunta):
    caracteres = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\'\-]+$")
    while True:
        texto = input(pregunta).strip()
        if texto == "":
            print(" my bro, eso no sirve. ")
            continue
        if caracteres.fullmatch(texto):
            texto = " ".join(texto.split())
            texto = texto.title()
            return texto
        else:
            print(" eso no sirve. ")
# Funcion, que pregunta y valida. lo que ingresas, sea una de las dos opciones.
def pedir_genero():
    while True:
        genero = input("¿Es masculino o femenino?. ").strip().lower()
        if genero == "masculino" or genero == "femenino":
            return genero
        else:
            print(" no es un valor valido. ")
# Funcion, que pregunta y valida, mucho texto como: un diagnostico. 
def pedir_texto_largo(pregunta):
    caracteres = re.compile(r"^[0-9A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\'\-]+$")
    while True:
        mucho_texto = input(pregunta).strip()
        if mucho_texto == "":
            print(" my bro, eso no sirve. ")
            continue
        if caracteres.fullmatch(mucho_texto):
            mucho_texto = " ".join(mucho_texto.split())
            return mucho_texto
        else:
            print(" eso no sirve. ")
# En esta funcion, se integran, todas las anteriores funciones, para pregunta e ingrezar, los datos del pasiente, a un diccionario y luego este mismo, a una lista. 
def ingresar_pasiente():
    ID = int(str(uuid.uuid4().int)[:10]) # Genera una serie de dies numeros, para el ID
    nombre_completo = pedir_texto(" Ingreza el nombre completo del pasiente. ")
    genero = pedir_genero()
    diagnostico = pedir_texto_largo(" ¿Cual es el diagnostico, del pasiente?: ")
    historial = pedir_texto_largo(" ¿Cual es el historial, del pasiente?: ")
    diccionario = {
        "ID": ID, 
        "Nombre_completo": nombre_completo,  
        "Genero": genero,  
        "Diagnostico": diagnostico,
        "Historial": historial
        }  
    pacientes.append(diccionario)
    return print(f" pasiente ingresado correctamente: ID {ID} / nombre {nombre_completo} / genero {genero} / diagnostico {diagnostico} / historial {historial} ")
# Menu, el usuario, que permite ingresa, la cantidad de pasientes, que deses y cuando ya termines; salir de este Menu.  
while True:
    print(" 1. ingresar, un pasiente?")
    print(" 2, salir")
    try:
        opcion_2 = int(input(" ¿Que deceas hacer?. "))
    except ValueError:
        print("eso no es un numero, my bro. ")
        continue
    if opcion_2 == 1:
        ingresar_pasiente()
    elif opcion_2 == 2:
        break
    else:
        print(" mi compa, eso no esta en el menu, no joda. ")