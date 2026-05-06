# SYSTEM REPORT

import os
import subprocess
import sys


def run_automation():
    print(f"--- Reporte del Sistema en: {os.getcwd()} ---")  # [18]
    print(f"Directorio actual: {os.getcwd()}")

    try:
        print("Verificando espacio en disco...")

        resultado = subprocess.run(
            ["df", "-h"], capture_output=True, text=True
        )  # [12, 19]

        print(resultado.stdout)
        print(sys.version)

    except FileNotFoundError:
        print("X Error: El comando solicitado no se encuentra en el sistema")
    except Exception as e:
        print(f"X Ocurrio un error inesperado: {e}")


if __name__ == "__main__":
    run_automation()
