# MANAGE SERVERS


# Definimos una lista de servidores (nuestro Inventario inicial)
servers = ["192.168.1.10", "192.168.1.11", "192.168.1.2"]

print(f"Inventario inicial: {servers}")

# A veces necesitaremos agregar servidores dinamicamente
new_server = "192.168.1.59"
servers.append(new_server)  # Anade al final de la lista

# O eliminar uno que salio de mantenimiento
removed_server = servers.pop(0)  # Elimina el primero


print(f"Servidor fuera de servicio: {removed_server}")
print(f"Inventario actualizado ({len(servers)} servidores): {servers}")
