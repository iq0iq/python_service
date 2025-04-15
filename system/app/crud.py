from sqlalchemy.orm import Session
from . import models, schemas
import numpy as np
from datetime import timezone, datetime

def create_device_data(db: Session, data: schemas.DeviceDataCreate):
    db_data = models.DeviceData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_device_data(db: Session, device_id: str):
    return db.query(models.DeviceData).filter(models.DeviceData.device_id == device_id).all()

def analyze(data):
    if not data:
        return None
    x_values = [d.x for d in data]
    y_values = [d.y for d in data]
    z_values = [d.z for d in data]
    return {
        "min": {
            "x": min(x_values),
            "y": min(y_values),
            "z": min(z_values),
        },
        "max": {
            "x": max(x_values),
            "y": max(y_values),
            "z": max(z_values),
        },
        "count": len(data),
        "sum": {
            "x": sum(x_values),
            "y": sum(y_values),
            "z": sum(z_values),
        },
        "median": {
            "x": np.median(x_values),
            "y": np.median(x_values),
            "z": np.median(x_values),
        },
    }

def analyze_device_data_by_period(device_id: str, start_date: datetime, end_date: datetime, db: Session):
    start_date = start_date.astimezone(timezone.utc)
    end_date = end_date.astimezone(timezone.utc)
    data = db.query(models.DeviceData).filter(
        models.DeviceData.device_id == device_id,
        models.DeviceData.timestamp >= start_date,
        models.DeviceData.timestamp <= end_date
    ).all()
    return analyze(data)

def analyze_device_data(db: Session, device_id: str):
    data = get_device_data(db, device_id)
    return analyze(data)
