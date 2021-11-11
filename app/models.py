import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)

    bikes = relationship("Bike", back_populates="owner")


class Bike(Base):
    __tablename__ = 'bikes'

    id = Column(String, primary_key=True, index=True)
    mark = Column(String, index=True)
    model = Column(String, index=True)
    owner_id = Column(String, ForeignKey("clients.id"))

    owner = relationship("Client", back_populates='bikes')
