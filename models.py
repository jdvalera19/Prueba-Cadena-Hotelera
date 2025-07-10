from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import declarative_base, relationship

# Declaramos el ORM base
Base = declarative_base()

# Tabla Hotel
class Hotel(Base):
    __tablename__ = "hotel"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)

    habitaciones = relationship("Habitacion", back_populates="hotel")

    def __repr__(self):
        return f"<Hotel(id={self.id}, nombre='{self.nombre}', ciudad='{self.ciudad}')>"
        
    
#Tabla Habitacion
class Habitacion(Base):
    __tablename__ = "habitacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotel.id'), nullable=False)
    tipo = Column(String, nullable=False)         # estándar, premium, VIP
    capacidad = Column(Integer, nullable=False)   # número máximo de personas

    hotel = relationship("Hotel", back_populates="habitaciones")
    disponibilidades = relationship("Disponibilidad", back_populates="habitacion")    
    reservas = relationship("Reserva", back_populates="habitacion")


#Tabla Disponibilidad
class Disponibilidad(Base):
    __tablename__ = "disponibilidad"
    id = Column(Integer, primary_key=True)
    habitacion_id = Column(Integer, ForeignKey("habitacion.id"))
    fecha = Column(Date, nullable=False)
    disponible = Column(Boolean, default=True)

    habitacion = relationship("Habitacion", back_populates="disponibilidades")

#Tabla Cliente
class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)

    reservas = relationship("Reserva", back_populates="cliente")

# Tabla Reserva
class Reserva(Base):
    __tablename__ = "reserva"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    habitacion_id = Column(Integer, ForeignKey('habitacion.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="reservas")
    habitacion = relationship("Habitacion", back_populates="reservas")    
