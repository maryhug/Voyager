from Clinic.Add import *
from Clinic.Search import *
from Clinic.Update import *
from Clinic.Delete import eliminar_paciente_por_id, imprimir_paciente
from Clinic.Report import (
    reporte_todos_los_pacientes,
    reporte_pacientes_mayores_de_60,
    reporte_diagnosticos_frecuentes,
    reporte_cantidad_total
)

def menu():
    print()
    print("\n=== MENU ===")
    print("1. Registrar pacientes")
    print("2. Buscar pacientes")
    print("3. Listar pacientes")
    print("4. Actualizar Datos")
    print("5. Eliminar pacientes")
    print("6. Reportes")
    print("7. Salir")

def main():
    while True:
        menu()
        opcion = input("Escribe una opción: ").strip()
        if opcion == "1":
            ingresar_paciente()
            pregunta = input("Deseas ingresar otro paciente? (si - no) : ").capitalize()
            if pregunta == "si".capitalize():
                ingresar_paciente()
        elif opcion == "2":
            buscar_pacientes()
        elif opcion == "3":
            reporte_todos_los_pacientes(pacientes)
        elif opcion == "4":
            actualizar_paciente(pacientes)
        elif opcion == "5":
            eliminado = eliminar_paciente_por_id(pacientes, input("ID a eliminar: "))
            if eliminado:
                print("\nPaciente eliminado (datos):")
                imprimir_paciente(eliminado)
        elif opcion == "6":
            reporte_todos_los_pacientes(pacientes)
            reporte_pacientes_mayores_de_60(pacientes)
            reporte_diagnosticos_frecuentes(pacientes)
            reporte_cantidad_total(pacientes)
        elif opcion == "7":
            print("Saliendo de la aplicación!!")
            break
        else:
            print("La opción no es válida")

if __name__ == "__main__":
    main()
