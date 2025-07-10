from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Reemplaza estos valores con los de tu base de datos
USER = 'postgres'     
PASSWORD = 'admin123'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'reservas_hoteles'

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crea una sesión (opcional, para consultar datos después)
SessionLocal = sessionmaker(bind=engine)

# Crear todas las tablas definidas en models.py
def crear_tablas():
    Base.metadata.create_all(bind=engine)

