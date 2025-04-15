from pydantic import BaseModel
from datetime import datetime

class DeviceDataCreate(BaseModel):
    device_id: str
    x: float
    y: float
    z: float
    timestamp: datetime

class DeviceData(DeviceDataCreate):
    id: int

    class Config:
        orm_mode = True