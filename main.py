#Conexion a la base de datos con fastapi y sqlalchemy
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Hotel
from pydantic import BaseModel

app = FastAPI()

#Conexion a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD para Hotel

# GET
@app.get("/hoteles/")
def listar_hoteles(db: Session = Depends(get_db)):
    hoteles = db.query(Hotel).all()
    return hoteles

# CREAR HOTEL
class HotelCreate(BaseModel):
    nombre: str
    ciudad: str

# POST
@app.post("/hoteles/")
def crear_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    nuevo = Hotel(nombre=hotel.nombre, ciudad=hotel.ciudad)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo          

# PUT
@app.put("/hoteles/{hotel_id}")
def editar_hotel(hotel_id: int, hotel: HotelCreate, db: Session = Depends(get_db)):
    hotel_existente = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel_existente:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")
    
    hotel_existente.nombre = hotel.nombre
    hotel_existente.ciudad = hotel.ciudad
    db.commit()
    return hotel_existente

# DELETE
@app.delete("/hoteles/{hotel_id}")
def eliminar_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel_existente = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel_existente:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")
    
    db.delete(hotel_existente)
    db.commit()
    return {"detail": "Hotel eliminado exitosamente"}