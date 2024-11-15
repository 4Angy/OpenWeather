# Usa la imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto en el contenedor
COPY . .

# Instala las dependencias del proyecto (si tienes un archivo requirements.txt)
 RUN pip install -r requirements.txt

# Ejecuta tu archivo Python
CMD ["python", "app.py"]