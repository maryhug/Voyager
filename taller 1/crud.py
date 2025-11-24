"""Simport csv
import os
import json


class CRUD:

    # ---------------------------------------------------------
    # CREAR ARCHIVO CSV SI NO EXISTE
    # ---------------------------------------------------------
    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "edad"])

    # ---------------------------------------------------------
    # OBTENER NUEVO ID AUTOMÁTICO
    # ---------------------------------------------------------
    def obtener_nuevo_id(self, archivo):
        with open(archivo, "r") as f:
            filas = list(csv.reader(f))

        if len(filas) == 1:   # Solo tiene encabezado
            return 1

        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1

    # ---------------------------------------------------------
    # CREAR PERSONA
    # ---------------------------------------------------------
    def crear(self, archivo, nombre, edad):
        id_nuevo = self.obtener_nuevo_id(archivo)
        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id_nuevo, nombre, edad])
        return id_nuevo

    # ---------------------------------------------------------
    # LISTAR DATOS
    # ---------------------------------------------------------
    def listar(self, archivo):
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Saltar encabezado
            return list(reader)

    # ---------------------------------------------------------
    # ACTUALIZAR PERSONA
    # ---------------------------------------------------------
    def actualizar(self, archivo, id_buscar, nuevo_nombre, nueva_edad):
        filas_actualizadas = []
        actualizado = False

        with open(archivo, "r") as f:
            reader = csv.reader(f)
            encabezado = next(reader)
            for fila in reader:
                if fila[0] == id_buscar:
                    fila[1] = nuevo_nombre
                    fila[2] = nueva_edad
                    actualizado = True
                filas_actualizadas.append(fila)

        if actualizado:
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(encabezado)
                writer.writerows(filas_actualizadas)

        return actualizado

    # ---------------------------------------------------------
    # ELIMINAR PERSONA
    # ---------------------------------------------------------
    def eliminar(self, archivo, id_buscar):
        filas_nuevas = []
        eliminado = False

        with open(archivo, "r") as f:
            reader = csv.reader(f)
            encabezado = next(reader)
            for fila in reader:
                if fila[0] != id_buscar:
                    filas_nuevas.append(fila)
                else:
                    eliminado = True

        if eliminado:
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(encabezado)
                writer.writerows(filas_nuevas)

        return eliminado

    # ---------------------------------------------------------
    # GUARDAR A TXT
    # ---------------------------------------------------------
    def guardar_txt(self, archivo_csv, archivo_txt):
        datos = self.listar(archivo_csv)
        with open(archivo_txt, "w") as f:
            for d in datos:
                f.write(f"{d[0]}, {d[1]}, {d[2]}\n")

    # ---------------------------------------------------------
    # GUARDAR A JSON
    # ---------------------------------------------------------
    def guardar_json(self, archivo_csv, archivo_json):
        datos = self.listar(archivo_csv)
        lista_diccionarios = []

        for d in datos:
            lista_diccionarios.append({
                "id": d[0],
                "nombre": d[1],
                "edad": d[2]
            })

        with open(archivo_json, "w") as f:
            json.dump(lista_diccionarios, f, indent=4)
"""