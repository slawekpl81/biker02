from typing import List, Optional
from pydantic import BaseModel


class BikeBase(BaseModel):
    mark: str
    model: str


class BikeCreate(BikeBase):
    pass


class Bike(BikeBase):
    id: str
    owner_id: str

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    name: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: str
    bikes: List[Bike] = []

    class Config:
        orm_mode = True
