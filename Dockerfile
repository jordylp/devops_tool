#1. Usamos una imagen base de Python 
FROM python:3.9-slim

#2. Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

#3. Copiamos tus scripts actuales al interior del contenedor
COPY ./app

#4. Instalamos las dependencias (el Inspector pyest)
RUN pip install pytest

#5. El comando que se ejecutara al encender el contenedor
CMD ["python", "system_report.py"] 






