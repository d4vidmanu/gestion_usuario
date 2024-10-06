# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias del sistema necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copia todos los archivos del proyecto al directorio de trabajo
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --timeout=120 -r requirements.txt


# Exponer el puerto en el que corre FastAPI
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
