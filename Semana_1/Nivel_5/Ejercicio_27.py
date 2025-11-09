# Cajero automático.

PIN_CORRECTO = "1234"
saldo = 500.0
historial = []

def mostrar_menu_atm():
    print("\n=== Cajero Automático ===")
    print("1) Consultar saldo")
    print("2) Retirar")
    print("3) Depositar")
    print("4) Historial")
    print("5) Salir")

# Pedir PIN (3 intentos)
intentos = 0
autenticado = False
while intentos < 3:
    pin = input("Ingresa tu PIN (4 dígitos): ").strip()
    if pin == PIN_CORRECTO:
        autenticado = True
        break
    else:
        intentos += 1
        print(f"PIN incorrecto. Intentos restantes: {3 - intentos}")
if not autenticado:
    print("Se agotaron los intentos. Fin de sesión.")
else:
    while True:
        mostrar_menu_atm()
        op = input("Elige una opción: ").strip()
        if op == "1":
            print(f"Tu saldo es: ${saldo:.2f}")
        elif op == "2":
            monto = input("Monto a retirar: ").replace(',', '.').strip()
            while not (monto.replace('.', '', 1).isdigit() and monto.count('.') <= 1):
                monto = input("Monto inválido. Ingresa nuevamente: ").replace(',', '.').strip()
            monto = float(monto)
            if monto <= 0:
                print("Monto debe ser mayor que 0.")
            elif monto > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto
                historial.append(f"Retiro: -${monto:.2f}")
                print(f"Retiraste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
        elif op == "3":
            monto = input("Monto a depositar: ").replace(',', '.').strip()
            while not (monto.replace('.', '', 1).isdigit() and monto.count('.') <= 1):
                monto = input("Monto inválido. Ingresa nuevamente: ").replace(',', '.').strip()
            monto = float(monto)
            if monto <= 0:
                print("Monto debe ser mayor que 0.")
            else:
                saldo += monto
                historial.append(f"Depósito: +${monto:.2f}")
                print(f"Depositaste ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
        elif op == "4":
            if not historial:
                print("No hay transacciones.")
            else:
                print("\nHistorial de transacciones:")
                for t in historial:
                    print(" -", t)
        elif op == "5":
            print("Gracias por usar el cajero. Adiós.")
            break
        else:
            print("Opción inválida.")