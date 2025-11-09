## Fundamentos y Variables

### Ejercicio 1: Hola usuario
**Objetivo:** Interactuar con el usuario solicitando datos básicos (nombre y edad) y mostrarlos en pantalla.

**Lógica:**
- Solicita el nombre del usuario usando `input()` y lo convierte a string con `str()`
- Solicita la edad del usuario y la convierte a entero con `int()`
- Utiliza f-strings para formatear e imprimir un mensaje personalizado con los datos ingresados

---

### Ejercicio 2: Suma de dos números
**Objetivo:** Realizar una operación aritmética básica sumando dos números proporcionados por el usuario.

**Lógica:**
- Lee dos números del usuario convirtiéndolos a enteros con `int()`
- Almacena el resultado de la suma en la variable `add`
- Imprime el resultado de la operación

---

### Ejercicio 3: Área del triángulo
**Objetivo:** Calcular el área de un triángulo usando la fórmula: (base × altura) / 2

**Lógica:**
- Solicita la base y altura del triángulo, convirtiéndolas a `float()` para permitir decimales
- Aplica la fórmula matemática: `area = (base * altura) / 2`
- Muestra el resultado del área calculada

---

### Ejercicio 4: Conversor de grados Celsius a Fahrenheit
**Objetivo:** Convertir una temperatura de grados Celsius a Fahrenheit usando la fórmula de conversión.

**Lógica:**
- Solicita la temperatura en Celsius usando `float()` para aceptar decimales
- Aplica la fórmula de conversión: `F = C × 1.8 + 32`
- Imprime el resultado de la temperatura convertida a Fahrenheit

---

### Ejercicio 5: Tipo de dato
**Objetivo:** Demostrar el uso de la función `type()` para identificar el tipo de dato de diferentes variables.

**Lógica:**
- Utiliza `type()` para mostrar el tipo de dato de varios valores:
  - `32` → int (entero)
  - `True` → bool (booleano)
  - `9.5` → float (número decimal)
  - `"Hola mundo!!"` → str (cadena de texto)
  - `["Perro", "Gato", ...]` → list (lista)
- Imprime cada tipo de dato para que el usuario comprenda las diferentes categorías de variables en Python

---

### Ejercicio 6: Edad futura
**Objetivo:** Calcular y mostrar la edad que tendrá el usuario en el futuro (específicamente en 10 años).

**Lógica:**
- Solicita la edad actual del usuario convirtiéndola a entero
- Suma 10 años a la edad actual: `future = age + 10`
- Muestra el resultado de la edad futura calculada

---

## Conceptos clave trabajados
- **Entrada de datos:** uso de `input()` para interactuar con el usuario
- **Conversión de tipos:** `int()`, `float()`, `str()` para manejar diferentes tipos de datos
- **Operaciones aritméticas:** suma, multiplicación, división
- **Formato de strings:** uso de f-strings para mensajes dinámicos
- **Función `type()`:** identificación de tipos de datos en Python

# Comentarios explicativos para el README

## Condicionales y Control de Flujo

### Ejercicio 7: Mayor de edad
**Objetivo:** Determinar si una persona es mayor o menor de edad según su edad.

**Lógica:**
- Solicita la edad del usuario y la convierte a entero
- Utiliza una estructura condicional `if-else` para evaluar si la edad es mayor o igual a 18
- Si cumple la condición (`age >= 18`), imprime que es mayor de edad
- En caso contrario, imprime que es menor de edad

---

### Ejercicio 8: Número positivo, negativo o cero
**Objetivo:** Clasificar un número según sea positivo, negativo o cero.

**Lógica:**
- Lee un número entero del usuario
- Utiliza estructura `if-elif-else` para evaluar tres condiciones:
  - Si el número es exactamente 0 (`num == 0`)
  - Si el número es mayor que 0 (`num > 0`), es positivo
  - Si no cumple ninguna de las anteriores, es negativo
- Imprime la clasificación correspondiente

---

### Ejercicio 9: Par o impar
**Objetivo:** Determinar si un número es par o impar usando el operador módulo.

**Lógica:**
- Solicita un número entero al usuario
- Utiliza el operador módulo (`%`) para obtener el residuo de la división entre 2
- Si `num % 2 == 0`, el número es divisible entre 2, por lo tanto es par
- Si el residuo es diferente de 0, el número es impar

---

### Ejercicio 10: Calculadora básica
**Objetivo:** Crear una calculadora interactiva que realice las cuatro operaciones básicas con validación de errores.

**Lógica:**
- Implementa un bucle infinito `while True` para mantener la calculadora activa hasta que el usuario decida salir
- Muestra un menú con 5 opciones: suma, resta, multiplicación, división y salir
- Utiliza un bloque `try-except` para capturar errores de entrada (ValueError) cuando el usuario ingresa valores no numéricos
- Solicita dos números solo si la opción seleccionada no es "Salir" (opc != 5)
- Evalúa la opción seleccionada con estructura `if-elif-else`:
  - Opciones 1-4: realiza la operación aritmética correspondiente
  - Opción 4 (división): incluye validación adicional para evitar división entre cero
  - Opción 5: sale del programa con `break`
  - Cualquier otra opción: muestra mensaje de error
- Incluye separador visual (`"=" * 50`) para mejorar la legibilidad
- Utiliza `continue` para reiniciar el bucle cuando hay errores, sin terminar el programa

---

### Ejercicio 11: Clasificador de notas
**Objetivo:** Clasificar una nota numérica en categorías (Excelente, Aprobado, Reprobado) con validación robusta.

**Lógica:**
- Implementa un bucle `while True` que solo se rompe cuando se ingresa una nota válida
- Utiliza `try-except` para capturar errores cuando el usuario ingresa texto en lugar de números
- Solicita la nota como `float` para permitir decimales
- Evalúa la nota con estructura `if-elif-else`:
  - `0 <= note < 2.9`: Reprobado
  - `3.0 <= note < 4.9`: Aprobado
  - `note >= 5.0`: Excelente
  - Valores negativos: muestra mensaje de error
- Sale del bucle con `break` solo cuando la nota es válida y positiva
- Maneja errores de tipo (ValueError) mostrando un mensaje instructivo y reiniciando con `continue`

---

### Ejercicio 12: Mayor y menor de 3 números
**Objetivo:** Encontrar el valor máximo y mínimo entre tres números utilizando listas y funciones built-in.

**Lógica:**
- Crea una lista vacía para almacenar los números
- Utiliza un bucle `for` con `range(3)` para solicitar exactamente 3 números
- En cada iteración:
  - Solicita un número al usuario usando `i + 1` para mostrar la posición de manera amigable (1, 2, 3 en lugar de 0, 1, 2)
  - Agrega el número a la lista con `append()`
  - Imprime la lista actual para mostrar el progreso
- Utiliza las funciones built-in de Python:
  - `max(lista)`: encuentra el valor máximo
  - `min(lista)`: encuentra el valor mínimo
- Imprime ambos resultados

---

## Conceptos clave trabajados
- **Condicionales:** estructuras `if`, `elif`, `else` para tomar decisiones
- **Operadores de comparación:** `>=`, `==`, `>`, `<`
- **Operador módulo:** `%` para determinar divisibilidad
- **Bucles:** `while True` para crear menús interactivos
- **Control de flujo:** `break` y `continue` para controlar la ejecución de bucles
- **Manejo de excepciones:** `try-except` para capturar errores de entrada
- **Listas:** creación, método `append()`, y funciones `max()` y `min()`
- **Bucle `for` con `range()`:** iteración controlada
- **Validación de datos:** verificación de divisiones por cero y valores negativos

# Comentarios explicativos para el README

## Bucles y Estructuras de Repetición

### Ejercicio 13: Contar del 1 al 10
**Objetivo:** Imprimir números del 1 al 10 usando un bucle `for`.

**Lógica:**
- Utiliza `range(10)` que genera números del 0 al 9
- En cada iteración, imprime `i + 1` para mostrar números del 1 al 10
- Demuestra el uso básico del bucle `for` con `range()`

---

### Ejercicio 14: Sumatoria del 1 al n
**Objetivo:** Calcular la suma de todos los números del 1 hasta un número n dado por el usuario, usando la fórmula matemática de sumatoria.

**Lógica:**
- Implementa un bucle `while True` con validación robusta de entrada
- Utiliza `try-except` para capturar errores de tipo ValueError
- Valida que el número ingresado sea positivo (mayor o igual a 1)
- Usa `continue` para reiniciar el bucle si la validación falla
- Sale del bucle con `break` solo cuando la entrada es válida
- Aplica la fórmula de Gauss para sumatoria: `n × (n + 1) / 2`
- Utiliza división entera (`//`) para obtener un resultado entero
- Imprime el resultado usando f-string para mayor claridad

---

### Ejercicio 15: Tabla de multiplicar
**Objetivo:** Generar y mostrar la tabla de multiplicar de un número específico.

**Lógica:**
- Define una constante `hasta = 10` para establecer el límite de la tabla
- Implementa validación de entrada con `while True` y `try-except`
- Solicita al usuario qué tabla desea calcular
- Utiliza un bucle `for` con `range(1, hasta + 1)` para iterar del 1 al 10
- En cada iteración, calcula y muestra la multiplicación usando f-strings: `{multi} x {i} = {resultado}`
- Formatea la salida de manera clara y ordenada

---

### Ejercicio 16: Contador regresivo
**Objetivo:** Crear una cuenta regresiva desde un número dado hasta 1.

**Lógica:**
- Solicita al usuario el número inicial de la regresión
- Utiliza `range(reg, 0, -1)` con paso negativo para contar hacia atrás:
  - Inicia en `reg` (el número ingresado)
  - Termina en 1 (ya que el límite superior 0 no se incluye)
  - El paso `-1` indica que decrementa de uno en uno
- Imprime cada número con formato `- {número}` para mejor visualización

---

### Ejercicio 17: Adivina el número (juego)
**Objetivo:** Crear un juego interactivo donde el usuario debe adivinar un número aleatorio dentro de un rango con número limitado de intentos.

**Lógica:**
- Importa el módulo `random` para generar números aleatorios
- Solicita al usuario que defina el rango (mínimo y máximo) del juego
- Genera un número secreto aleatorio con `random.randint(minimo, maximo)`
- Define un número fijo de intentos (5)
- Utiliza un bucle `for` con `range(intentos)` para limitar las oportunidades
- En cada iteración:
  - Muestra el número de intento actual usando `i + 1`
  - Solicita un número al usuario
  - Compara el número ingresado con el número secreto
  - Si acierta, muestra mensaje de éxito y sale del bucle con `break`
  - Si no acierta, proporciona pistas indicando si el número secreto es mayor o menor
- Después del bucle, verifica si el usuario adivinó usando la última variable `adivina`
- Si no adivinó en los 5 intentos, revela el número secreto

---

### Ejercicio 18: Sumar hasta que el usuario escriba 0
**Objetivo:** Crear un sumador acumulativo que continúa pidiendo números hasta que el usuario ingrese 0.

**Lógica:**
- Inicializa `sumador = 0` para acumular la suma total
- Utiliza una bandera booleana (`bandera = True`) para controlar el bucle
- Implementa un bucle `while` que se ejecuta mientras la bandera sea verdadera
- Usa `.strip()` para eliminar espacios en blanco de la entrada
- Implementa validación con `try-except` para capturar entradas no numéricas
- Si hay un error de tipo, usa `continue` para reiniciar el bucle sin modificar la suma
- Verifica si el número ingresado es 0:
  - Si es 0: cambia la bandera a `False` y sale del bucle con `break`
  - Si no es 0: suma el número al acumulador usando `+=`
- Muestra la suma parcial después de cada número válido
- Al finalizar, muestra la suma total acumulada
- Demuestra el patrón de acumulación: `sumador += num` equivale a `sumador = sumador + num`

---

## Conceptos clave trabajados
- **Bucle `for` con `range()`:** iteración controlada con diferentes configuraciones
- **Parámetros de `range()`:** inicio, fin, y paso (positivo y negativo)
- **Bucle `while` con bandera:** control de flujo usando variables booleanas
- **Validación robusta:** combinación de `try-except`, `continue` y `break`
- **Módulo `random`:** generación de números aleatorios con `randint()`
- **Acumuladores:** variables que suman valores en cada iteración (`+=`)
- **Fórmulas matemáticas:** implementación de la fórmula de Gauss para sumatoria
- **F-strings:** formateo avanzado de salida con variables y expresiones
- **Lógica de juegos:** implementación de intentos limitados y sistema de pistas
- **Método `.strip()`:** limpieza de entrada de usuario
- **Bucles anidados:** validación dentro de bucles principales



# Comentarios explicativos para el README

## Listas y Estructuras de Datos

### Ejercicios 19, 20 y 21: Sistema de gestión de frutas (CRUD completo)
**Objetivo:** Crear un programa interactivo que permita administrar una lista de frutas con operaciones de Crear, Leer, Actualizar (Buscar) y Eliminar.

**Estructura general:**
- Define una lista global `frutas = []` para almacenar todas las frutas
- Implementa 4 funciones especializadas para cada operación
- Utiliza un menú principal con bucle `while` para mantener el programa activo

**Función `agregar()`:**
- Solicita al usuario cuántas frutas desea ingresar
- Implementa validación con `try-except` para asegurar entrada numérica
- Usa bucle `for` con `range(num)` para solicitar cada fruta
- Convierte las entradas a minúsculas con `.lower()` para consistencia
- Agrega cada fruta a la lista usando `append()`

**Función `eliminar()`:**
- Verifica primero si hay frutas en la lista con `if not frutas`
- Muestra las frutas disponibles antes de eliminar
- Solicita el nombre de la fruta a eliminar (convirtiendo a minúsculas)
- Verifica si la fruta existe con `if rem in frutas`
- Usa `remove()` para eliminar la primera coincidencia
- Muestra mensaje de error si la fruta no existe

**Función `listar()`:**
- Muestra todas las frutas almacenadas en la lista
- Verifica si la lista está vacía antes de mostrarla
- Imprime un mensaje apropiado según el estado de la lista

**Función `buscar()`:**
- Solicita el nombre de la fruta a buscar
- Utiliza el operador `in` para verificar si existe en la lista
- Muestra mensaje confirmando si se encontró o no la fruta

**Menú principal:**
- Inicializa `op = 1` para entrar al bucle
- Usa `while op != 5` para mantener el programa activo hasta que el usuario elija salir
- Muestra un menú numerado con 5 opciones
- Utiliza estructura `if-elif-else` para ejecutar la función correspondiente
- Llama a cada función según la opción seleccionada
- Sale del programa cuando `op == 5`

---

### Ejercicio 22: Lista de números y promedio
**Objetivo:** Calcular la suma y el promedio de una lista de números ingresados por el usuario.

**Lógica:**
- Inicializa dos variables: `lista = []` para almacenar números y `total = 0` como acumulador
- Solicita al usuario cuántos números desea ingresar
- Usa bucle `for` con `range(num)` para solicitar cada número
- Verifica que la entrada no esté vacía con `if valor != ""`
- Convierte cada entrada válida a entero y la agrega a la lista
- Implementa un segundo bucle `for` para recorrer la lista y acumular la suma:
  - `total += n` suma cada elemento al total
- Calcula el promedio dividiendo el total entre la cantidad de números: `promedio = total / num`
- Muestra los resultados usando f-strings multi-línea con `\n`

---

### Ejercicio 23: Números pares
**Objetivo:** Filtrar y almacenar únicamente los números pares de una lista ingresada por el usuario.

**Lógica:**
- Crea una lista vacía `pares = []` para almacenar solo números pares
- Solicita cuántos números se ingresarán
- Implementa un bucle `for` anidado con validación:
  - Bucle externo: itera según la cantidad de números (`range(num)`)
  - Bucle interno `while True`: valida que la entrada sea numérica
  - Usa `try-except` para capturar errores de conversión
  - Sale del bucle interno con `break` solo cuando la entrada es válida
- Verifica si el número es par usando el operador módulo: `if valor % 2 == 0`
- Agrega a la lista `pares` solo si cumple la condición de paridad
- Imprime la lista final de números pares

---

### Ejercicio 24: Eliminar duplicados
**Objetivo:** Extender el ejercicio anterior para ofrecer la opción de eliminar números duplicados de la lista de pares.

**Lógica:**
- Reutiliza el código del ejercicio 23 para obtener la lista de números pares
- Solicita al usuario si desea eliminar duplicados (S/N)
- Convierte la respuesta a minúsculas con `.lower()` para comparación flexible
- Si el usuario confirma (`if duplicados in "S".lower()`):
  - Crea un conjunto `visto = set()` para rastrear números ya procesados
  - Crea una lista `resultado = []` para almacenar números únicos
  - Recorre cada elemento de la lista `pares`:
    - Verifica si el número NO está en el conjunto con `if o not in visto`
    - Si es nuevo: agrega al conjunto con `add()` y a la lista resultado con `append()`
    - Si ya existe: lo omite (eliminando el duplicado)
  - Imprime la nueva lista sin duplicados
- Si el usuario rechaza, simplemente muestra mensaje de confirmación

**Técnica clave:**
- Usa un `set()` para verificación rápida de existencia (O(1) vs O(n) de listas)
- Mantiene una lista separada para preservar el orden de inserción
- Demuestra el algoritmo manual de eliminación de duplicados sin usar funciones built-in

---

## Conceptos clave trabajados
- **Listas:** creación, métodos `append()`, `remove()`, y acceso con `in`
- **Funciones:** definición con `def`, encapsulación de lógica específica
- **Variables globales:** uso de lista compartida entre funciones
- **Operador `in`:** búsqueda de elementos en listas
- **Operador `not`:** negación lógica (`if not frutas`)
- **CRUD:** operaciones básicas de Create, Read, Update, Delete
- **Menús interactivos:** bucle `while` con opciones numeradas
- **Acumuladores:** variables que suman valores progresivamente
- **Filtrado de datos:** selección de elementos según condiciones
- **Sets (conjuntos):** estructura de datos para elementos únicos
- **Algoritmo de eliminación de duplicados:** técnica manual preservando orden
- **Métodos de string:** `.lower()` para normalización de texto
- **Validación anidada:** bucles `while` dentro de bucles `for`
- **F-strings multi-línea:** formato de salida complejo con `\n`