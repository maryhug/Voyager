frutas = []

while True:
    print(f"\n Frutas: {frutas}\n")
    print("1. Agregar fruta")
    print("2. Eliminar fruta")
    print("3. Salir")
    
    opcion = input("\nOpción: ")
    
    if opcion == "1":
        fruta = input("Nombre de la fruta: ")
        frutas.append(fruta)
        print(f" {fruta} agregada")
    
    elif opcion == "2":
        fruta = input("¿Qué fruta eliminar? ")
        if fruta in frutas:
            frutas.remove(fruta)
            print(f" {fruta} eliminada")
        else:
            print(f" {fruta} no está en la lista")
    
    elif opcion == "3":
        print("Adiós")
        break