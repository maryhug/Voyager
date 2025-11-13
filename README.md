# Taller: Sistema de Gestión de Pacientes — “ClinicManager”

## 👥 Integrantes del Proyecto

| Integrante | Funcionalidad Principal | Descripción del Aporte |
|-------------|--------------------------|-------------------------|
| **Maryhug** | Estructura general / Eliminar / Reportes | Diseñó la estructura modular del sistema, creó funciones de validación de datos y garantizó el correcto manejo de entradas del usuario. |
| **Santiago** | Actualizar Pacientes | Implementó la función para registrar pacientes nuevos, evitando duplicados y asegurando la integridad de la información. |
| **Samuel** | Buscar | Desarrolló las funciones para buscar pacientes por ID, nombre o diagnóstico, además de la eliminación controlada de registros. |
| **Jhon** | Agregar pacientes | Programó la actualización de datos de pacientes y el listado con formato organizado para mostrar la información guardada. |
| **Todo el equipo** | Integración y pruebas | Participó en la integración del sistema, pruebas de funcionamiento y documentación del proyecto. |


## Funciones Utilizados 
| Función / Módulo        | ¿Para qué sirve?                                                                 | ¿Dónde se usa?                                        | Ejemplo |
|--------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------|----------|
| `import uuid`            | Permite generar identificadores únicos universales (UUID).                      | En sistemas que necesitan IDs únicos (ej: pacientes).  | `import uuid` |
| `import re`              | Importa el módulo de expresiones regulares para validar y buscar patrones.      | Validación de texto, correos, números, etc.            | `import re` |
| `.capitalize()`          | Convierte la primera letra de una cadena en mayúscula.                          | Formatear nombres o textos.                            | `"maria".capitalize()` → `"Maria"` |
| `.strip()`               | Elimina espacios al inicio y al final de una cadena.                            | Limpieza de entradas del usuario.                      | `" hola ".strip()` → `"hola"` |
| `Counter()`              | Cuenta elementos repetidos en una lista o cadena.                               | Estadísticas o frecuencia de elementos.                | `Counter("banana")` → `{'b':1,'a':3,'n':2}` |
| `len()`                  | Retorna la longitud (cantidad de elementos) de un objeto.                       | Saber cuántos datos hay en una lista o texto.          | `len([1,2,3])` → `3` |
| `.get()`                 | Obtiene el valor de una clave en un diccionario, evitando errores si no existe. | Lectura segura de datos en diccionarios.               | `paciente.get("nombre", "Desconocido")` |
| `.most_common()`         | Devuelve los elementos más comunes de un `Counter`.                             | Contar y mostrar los más frecuentes.                   | `Counter("banana").most_common(1)` → `[('a',3)]` |
| `any()`                  | Retorna `True` si al menos un elemento de un iterable es verdadero.              | Validaciones múltiples en listas o condiciones.         | `any([False, True, False])` → `True` |
| `isinstance()`           | Verifica si un objeto es de un tipo de dato específico.                         | Validación de tipos de variables.                      | `isinstance(5, int)` → `True` |
| `.append()`              | Agrega un elemento al final de una lista.                                       | Añadir nuevos datos a listas.                          | `lista.append("nuevo")` |
| `.pop()`                 | Elimina y retorna el último elemento de una lista.                              | Eliminar elementos específicos.                        | `lista.pop()` |
| `.lower()`               | Convierte toda la cadena a minúsculas.                                          | Comparaciones o normalización de texto.                | `"HOLA".lower()` → `"hola"` |
| `uuid.uuid4()`           | Genera un UUID único aleatorio (versión 4).                                     | Asignar identificadores únicos.                        | `id = uuid.uuid4()` |
| `.title()`               | Convierte cada palabra de una cadena en mayúscula inicial.                      | Formatear nombres completos o títulos.                 | `"ana maria".title()` → `"Ana Maria"` |
| `.join()`                | Une elementos de una lista en una sola cadena con un separador.                 | Crear textos a partir de listas.                       | `", ".join(["Ana","Luis"])` → `"Ana, Luis"` |
| `.split()`               | Divide una cadena en una lista según un separador.                              | Procesar texto en partes.                              | `"Ana,Luis".split(",")` → `["Ana","Luis"]` |
| `re.fullmatch()`         | Comprueba si toda la cadena cumple un patrón regex.                             | Validar formato completo (ej: nombres, correos).       | `re.fullmatch(r"[A-Za-z]+", "Maria")` |
| `re.compile()`           | Compila un patrón regex para reutilizarlo varias veces.                         | Optimizar validaciones repetitivas.                    | `patron = re.compile(r"\d+")` |
