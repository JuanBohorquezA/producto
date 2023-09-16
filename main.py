# Definir listas para almacenar usuarios y préstamos
usuarios = []
prestamos = []

# Función para registrar un usuario
def registrar_usuario(nombre, numero_tarjeta):
    usuario = {"nombre": nombre, "numero_tarjeta": numero_tarjeta}
    usuarios.append(usuario)

# Función para tomar una bicicleta en préstamo
def tomar_bicicleta(numero_tarjeta, origen, destino):
    usuario = None
    for u in usuarios:
        if u["numero_tarjeta"] == numero_tarjeta:
            usuario = u
            break

    if usuario:
        prestamo = {"usuario": usuario, "origen": origen, "destino": destino}
        prestamos.append(prestamo)
        print(f"{usuario['nombre']} ha tomado una bicicleta en préstamo de {origen} a {destino}.")
    else:
        print("Usuario no encontrado.")

# Función para consultar el listado de usuarios
def consultar_usuarios():
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Número de Tarjeta: {usuario['numero_tarjeta']}")

# Función para consultar el listado de préstamos
def consultar_prestamos():
    for prestamo in prestamos:
        print(f"Usuario: {prestamo['usuario']['nombre']}, Origen: {prestamo['origen']}, Destino: {prestamo['destino']}")

# Ejemplo de uso
registrar_usuario("Juan Perez", "12345")
registrar_usuario("Ana Lopez", "67890")

tomar_bicicleta("12345", "Estación A", "Estación B")
tomar_bicicleta("67890", "Estación C", "Estación D")

consultar_usuarios()
consultar_prestamos()
