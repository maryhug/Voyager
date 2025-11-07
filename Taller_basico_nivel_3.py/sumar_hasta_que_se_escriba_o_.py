while True:
    numero1 = int(input("Ingresa el primer número (0 para salir): "))
    
    if numero1 == 0:  # ← Cambio: numero1 (no "numero")
        print("👋 ¡Adiós!")
        break
    
    numero2 = int(input("Ingresa el segundo número: "))
    suma = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {suma}\n")