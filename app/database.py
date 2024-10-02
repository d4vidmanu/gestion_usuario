from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la URL de tu base de datos PostgreSQL local
DATABASE_URL = "postgresql://postgres:Manuel_1223@localhost/gestion_usuarios"

# Crea el motor de conexión
engine = create_engine(DATABASE_URL)

# Crea una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
