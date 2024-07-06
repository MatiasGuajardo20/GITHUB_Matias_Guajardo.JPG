import datetime

clientes = {}
compras = {}
id_cliente = 1

def registrar_cliente():
    global id_cliente
    nombre = input("Ingrese el nombre del cliente: ").strip().upper()
    apellido = input("Ingrese el apellido del cliente: ").strip().upper()
    correo = input("Ingrese el correo electrónico del cliente: ").strip()
    
    if not nombre or not apellido or not correo:
        print("Todos los campos son obligatorios. Intente nuevamente.")
        return
    
    clientes[id_cliente] = {"nombre": nombre, "apellido": apellido, "correo": correo}
    compras[id_cliente] = []
    print(f"Cliente registrado con éxito. ID asignado: {id_cliente}")
    id_cliente += 1

def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print("ID\tNombre\t\tCorreo")
    for id_cliente, info in clientes.items():
        print(f"{id_cliente}\t{info['nombre']} {info['apellido']}\t{info['correo']}")

def registrar_compra():
    id_cliente = int(input("Ingrese el ID del cliente: "))
    if id_cliente not in clientes:
        print("ID de cliente no encontrado. Intente nuevamente.")
        return
    
    fecha = input("Ingrese la fecha de la compra (AAAA-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        print("Fecha en formato incorrecto. Intente nuevamente.")
        return
    
    monto = float(input("Ingrese el monto total de la compra: ").strip())
    puntos = int(monto * 0.01)
    compras[id_cliente].append({"fecha": fecha, "monto": monto, "puntos": puntos})
    print(f"Compra registrada con éxito. Puntos acumulados: {puntos}")

def listar_compras_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))
    if id_cliente not in clientes:
        print("ID de cliente no encontrado. Intente nuevamente.")
        return
    
    print(f"ID CLIENTE: {id_cliente}")
    print(f"NOMBRE CLIENTE: {clientes[id_cliente]['nombre']} {clientes[id_cliente]['apellido']}")
    print("Fecha de Compra\tMonto Total\tPuntos")
    
    total_puntos = 0
    for compra in compras[id_cliente]:
        print(f"{compra['fecha']}\t{compra['monto']}\t{compra['puntos']}")
        total_puntos += compra['puntos']
    
    print(f"PUNTOS TOTALES A CANJEAR: {total_puntos} pesos")
    
    with open(f"RESUMEN_CLIENTE_ID_{id_cliente}.txt", "w") as file:
        file.write(f"ID CLIENTE: {id_cliente}\n")
        file.write(f"NOMBRE CLIENTE: {clientes[id_cliente]['nombre']} {clientes[id_cliente]['apellido']}\n")
        file.write("Fecha de Compra\tMonto Total\tPuntos\n")
        for compra in compras[id_cliente]:
            file.write(f"{compra['fecha']}\t{compra['monto']}\t{compra['puntos']}\n")
        file.write(f"PUNTOS TOTALES A CANJEAR: {total_puntos} pesos\n")
    
    print(f"Resumen guardado en RESUMEN_CLIENTE_ID_{id_cliente}.txt")
