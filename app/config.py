import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "utec")
DB_HOST = os.getenv("DB_HOST", "18.213.167.234")  # Nueva IP
DB_NAME = os.getenv("DB_NAME", "gestion_usuarios")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{5432}/{DB_NAME}"
