from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: Optional[datetime] = None
    lokasi: str
    kuota: int

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    lokasi: Optional[str] = None
    kuota: Optional[int] = None

class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    date: datetime
    lokasi: str
    kuota: int

    model_config = {"from_attributes": True}