# 23 Cajero automático.

saldo = 100000  # Saldo inicial del usuario

while True:
    print("Bienvenido a cajeros.com My Broo.")
    print("1. Consultar saldo.")
    print("2. Retirar dinero.")
    print("3. Depositar dinero.")
    print("4. Salir.")
    
    try:
        opcion = int(input("¿Qué deseas hacer mi compaaa? "))
        
        if opcion == 1:
            # Muestra el saldo disponible
            print(f"Tu saldo actual es de ${saldo}.")
            
        elif opcion == 2:
            # Permite retirar dinero del saldo
            retiro = int(input("¿Cuánto dinero deseas retirar? "))
            if retiro > saldo:
                print("Mi compaaa, no tienes tanto dinero.")
            elif retiro <= 0:
                print("Eso no tiene sentido mi compaaa.")
            else:
                saldo -= retiro
                print(f"Retiraste ${retiro}. Tu nuevo saldo es ${saldo}.")
                
        elif opcion == 3:
            # Permite agregar dinero al saldo
            deposito = int(input("¿Cuánto dinero vas a depositar? "))
            if deposito <= 0:
                print("Eso no se puede mi compaaa.")
            else:
                saldo += deposito
                print(f"Depositaste ${deposito}. Tu nuevo saldo es ${saldo}.")
                
        elif opcion == 4:
            # Sale del programa
            print("Gracias por usar el cajero mi compaaa. Dios te bendiga.")
            break
        
        else:
            print("Mi compaaa, esa opción no existe.")
            
    except ValueError:
        # Si el usuario escribe algo que no sea número
        print("Eso no es un número mi compaaa.")