import todoahorro 

def menu():
    while True:
        print("\nmenu elija una opcion:")
        print("1. registrar cliente")
        print("2. listar clientes registrados")
        print("3. registrar compra")
        print("4. listar compras de un cliente")
        print("5. salir del programa")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            todoahorro.registrar_cliente()
        elif opcion == "2":
            todoahorro.listar_clientes()
        elif opcion == "3":
            todoahorro.registrar_compra()
        elif opcion == "4":
            todoahorro.listar_compras_cliente()
        elif opcion == "5":
            print("Gracias por utilizar el sistema de TODOAHORRO. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
