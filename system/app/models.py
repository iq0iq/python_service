from sqlalchemy import Column, Float, Integer, String, DateTime
from .database import Base
from datetime import datetime

class DeviceData(Base):
    __tablename__ = "device_data"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)