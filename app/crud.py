import uuid

from sqlalchemy.orm import Session

from . import models, schemas


def get_client_by_id(db: Session, client_id: str):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_clients_by_name(db: Session, client_name: str):
    return db.query(models.Client).filter(models.Client.name == client_name).all()


def get_clients(db: Session, skip: int = 0, limit: int = 10):
    """get all clients"""
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(id=str(uuid.uuid4()), name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_bike(db: Session, bike: schemas.BikeCreate):
    db_bike = models.Bike(id=str(uuid.uuid4()),
                          mark=bike.mark, model=bike.model,
                          owner_id=bike.owner_id)
    db.add(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike


def get_bikes(db: Session, skip: int = 0, limit: int = 10):
    """get all bikes"""
    return db.query(models.Bike).offset(skip).limit(limit).all()
