import os
import sys
import subprocess


def run_automation():
    print(f"--- Reporte del Sistema en: {os.getcwd()} ---")  #

    print("Verificando espacio en disco...")
    resultado = subprocess.run(["df", "-h"], capture_output=True, text=True)  # [12, 19]

    print(resultado.stdout)
    print(sys.version)


if __name__ == "__main__":
    run_automation()
