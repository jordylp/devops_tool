# MANAGE SERVERS


# Definimos una lista de servidores (nuestro Inventario inicial)
servers = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

print(f"Inventario inicial: {servers}")

# A veces necesitaremos agregar servidores dinamicamente
web_server_prod = "192.168.1.60"
servers.append(web_server_prod)  # Anade al final de la lista


# O eliminar uno que salio de mantenimiento
removed_server = servers.pop(0)  # Elimina el primero


print(f"Servidor fuera de servicio: {removed_server}")
print(f"Inventario actualizado ({len(servers)} servidores): {servers}")
