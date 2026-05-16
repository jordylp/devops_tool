# Definimos un diccionario con el estado de nuestros servidores
"""

server_status = {
    "web_prod": "activo",
    "db_prod": "manteinimiento",
    "cache_dev": "inactivo",
}


def check_status(server_name):
    # Usamos .get() para evitar que el programa falle si la clave no existe
    estado = server_status.get(server_name, "servidor no encontrado ")
    print(f"El estado del servidor [{server_name}] es: {estado}")


if __name__ == "__main__":
    # Prueba con un servidor que existe
    check_status("web_prod")
    # Prueba con uno que NO existe
    check_status("correo_test")

"""

server_status = {
    "web_prod": "activo",
    "db_prod": "mantenimiento",
    "cache_dev": "inactivo",
}


def check_status(server_name):
    # Usamos .get() para evitar que el programa falle si la clave no existe
    estado = server_status.get(server_name, "servidor no encontrado ")
    print(f"El estado del servidor [{server_name}] es: {estado}")


if __name__ == "__main__":
    # Prueba con un servidor  que existe
    # Prueba con uno que No existe
    check_status("web_prod")
