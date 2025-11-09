# Cajero automático.

# Constante que almacena el PIN correcto para autenticación
PIN_CORRECTO = "1234"

# Variable que almacena el saldo actual de la cuenta
saldo = 500.0

# Lista que registra todas las transacciones (retiros y depósitos)
historial = []

# Muestra el menú principal del cajero automático.
def mostrar_menu_atm():
    print("\n=== Cajero Automático ===")
    print("1) Consultar saldo")
    print("2) Retirar")
    print("3) Depositar")
    print("4) Historial")
    print("5) Salir")


# El usuario tiene 3 intentos para ingresar el PIN correcto
intentos = 0
autenticado = False

# Bucle de autenticación
while intentos < 3:
    pin = input("Ingresa tu PIN (4 dígitos): ").strip()

    # Verificar si el PIN ingresado coincide con el correcto
    if pin == PIN_CORRECTO:
        autenticado = True
        break   # Salir del bucle si el PIN es correcto
    else:
        intentos += 1
        # Mostrar intentos restantes
        print(f"PIN incorrecto. Intentos restantes: {3 - intentos}")

# Si no se autenticó después de 3 intentos, terminar el programa
if not autenticado:
    print("Se agotaron los intentos. Fin de sesión.")
else:
    # Opciones del menú
    # Solo se ejecuta si la autenticación fue exitosa
    while True:
        mostrar_menu_atm()
        opcion = input("Elige una opción: ").strip()

        # Opción 1: Consultar saldo actual
        if opcion == "1":
            # Mostrar saldo con formato de 2 decimales
            print(f"Tu saldo es: ${saldo:.2f}")

        # Opción 2: Retirar dinero
        elif opcion == "2":
            # Solicitar monto con validación de formato
            monto = input("Monto a retirar: ").replace(',', '.').strip()

            # Validar que el monto sea un número válido
            while not (monto.replace('.', '', 1).isdigit() and monto.count('.') <= 1):
                monto = input("Monto inválido. Ingresa nuevamente: ").replace(',', '.').strip()
            monto = float(monto)

            # Validar que el monto sea positivo
            if monto <= 0:
                print("Monto debe ser mayor que 0.")
            # Validar que haya fondos suficientes
            elif monto > saldo:
                print("Fondos insuficientes.")
            else:
                # Realizar el retiro
                saldo -= monto
                # Registrar la transacción en el historial
                historial.append(f"Retiro: -${monto:.2f}")
                print(f"Retiraste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")

        # Opción 3: Depositar dinero
        elif opcion == "3":
            # Solicitar monto con validación de formato
            monto = input("Monto a depositar: ").replace(',', '.').strip()

            # Validar que el monto sea un número válido
            while not (monto.replace('.', '', 1).isdigit() and monto.count('.') <= 1):
                monto = input("Monto inválido. Ingresa nuevamente: ").replace(',', '.').strip()
            monto = float(monto)

            # Validar que el monto sea positivo
            if monto <= 0:
                print("Monto debe ser mayor que 0.")
            else:
                # Realizar el depósito
                saldo += monto
                # Registrar la transacción en el historial
                historial.append(f"Depósito: +${monto:.2f}")
                print(f"Depositaste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")

        # Opción 4: Mostrar historial de transacciones
        elif opcion == "4":
            if not historial:
                print("No hay transacciones.")
            else:
                print("\nHistorial de transacciones:")
                # Iterar sobre cada transacción registrada
                for t in historial:
                    print(" -", t)

        # Opción 5: Salir del cajero
        elif opcion == "5":
            print("Gracias por usar el cajero. Adiós.")
            # Terminar el bucle principal y cerrar sesión
            break

        # Opción inválida
        else:
            print("Opción inválida.")