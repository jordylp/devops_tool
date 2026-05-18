# check_ip
import sys


# Inventario fijo
inventario = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]


def audit_ip():
    # len(sys.argv) nos dice cuantos elementos hay en la maleta
    if len(sys.argv) < 2:
        print("❌ Error: Debes proporcionar una IP. Uso: python3 check_ip.py <ip>")
        sys.exit(1)  # Finaliza el script on error [6, 7]

    ip_a_buscar = sys.argv[1]

    if ip_a_buscar in inventario:
        print(f"✅  La IP {ip_a_buscar} es parte del inventario oficial.")
    else:
        print(f"⚠️ Alerta: {ip_a_buscar} NO esta regristrada.")


if __name__ == "__main__":
    audit_ip()
