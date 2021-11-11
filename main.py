# uvicorn main:app --reload
from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def start():
    return {"message": "biker02"}


@app.post('/client', response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)


@app.get('/clients', response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10,
                 name: str = None,
                 db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    if name:
        clients = [client for client in clients if client.name == name]
    return clients


@app.post('/bike', response_model=schemas.Bike)
def create_bike(bike: schemas.BikeCreate, db: Session = Depends(get_db)):
    return crud.create_bike(db=db, bike=bike)


@app.get('/bikes', response_model=List[schemas.Bike])
def read_bikes(skip: int = 0, limit: int = 10,
               mark: str = None,
               owner_name: str = None,
               db: Session = Depends(get_db)):
    bikes = crud.get_bikes(db, skip=skip, limit=limit)
    if mark:
        bikes = [bike for bike in bikes if bike.mark == mark]
    if owner_name:
        """get bikes by owner name"""
        clients = crud.get_clients_by_name(db, owner_name)
        clients = [client.id for client in clients]
        bikes = [bike for bike in bikes if bike.owner_id in clients]
    return bikes
