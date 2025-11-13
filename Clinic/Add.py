import uuid
import re

pacientes = []

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
            print("Eso no parece un nombre válido. Usa solo letras o espacios.")

def pedir_genero():
    while True:
        genero = input("¿Es Masculino o Femenino? ").strip().capitalize()
        if genero in ("masculino", "femenino", "fem", "mas", "f", "m"):
            return genero.capitalize()
        else:
            print("Debes escribir 'masculino' - 'femenino'")


def pedir_texto_largo(pregunta):
    caracteres = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\.\'\-]+$")
    while True:
        mucho_texto = input(pregunta).strip()
        if mucho_texto == "":
            print(" my bro, eso no sirve. ")
            continue
        if caracteres.fullmatch(mucho_texto):
            mucho_texto = " ".join(mucho_texto.split())
            return mucho_texto
        else:
            print("Ingresa un texto válido.")

def ingresar_paciente():
    ID = int(str(uuid.uuid4().int)[:10])  # Genera un ID de diez números.
    nombre_completo = pedir_texto("Ingresa el nombre completo del paciente: ").capitalize()
    genero = pedir_genero()
    diagnostico = pedir_texto_largo("¿Cuál es el diagnóstico del paciente?: ").capitalize()
    historial = pedir_texto_largo("¿Cuál es el historial del paciente?: ").capitalize()
    edad = perdir_numero_entero("Ingresa la edad del paciente: ")

    historial = [historial] if historial else []

    diccionario = {
        "ID": ID,
        "Nombre_completo": nombre_completo,
        "Genero": genero,
        "Diagnostico": diagnostico,
        "Historial": historial,
        "Edad": edad
    }

    pacientes.append(diccionario)
    print("Paciente ingresado correctamente:")
    print(f"   ID: {ID} | Nombre: {nombre_completo} | Género: {genero} | "
          f"Diagnóstico: {diagnostico} | Historial: {historial} | Edad: {edad}")