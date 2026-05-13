from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    lokasi = Column(String, nullable=False, default="")
    kuota = Column(Integer, nullable=False, default=0)