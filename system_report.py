# SYSTEM REPORT

import os
import subprocess


def run_automation():
    print(f"--- Reporte del Sistema en: {os.getcwd()} ---")  # [18]

    # Ejecutamos un comando de linux desde python
    # 'df -h' muestra el espacio en disco de forma legible
    print("Verificando espacio en disco...")
    resultado = subprocess.run(["df", "-h"], capture_output=True, text=True)  # [12, 19]

    print(resultado.stdout)


if __name__ == "__main__":
    run_automation()
