from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import database, init_db, SessionLocal
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    init_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/data/", response_model=schemas.DeviceData)
def create_data(data: schemas.DeviceDataCreate, db: Session = Depends(get_db)):
    return crud.create_device_data(db=db, data=data)

@app.get("/data/{device_id}")
def read_data(device_id: str, db: Session = Depends(get_db)):
    data = crud.get_device_data(db=db, device_id=device_id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@app.get("/data/analyze/{device_id}")
def analyze_data(device_id: str, db: Session = Depends(get_db)):
    analysis = crud.analyze_device_data(db=db, device_id=device_id)
    return analysis


@app.get("/data/{device_id}/analyze_period")
def analyze_data_by_period(device_id: str, start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    data = crud.analyze_device_data_by_period(device_id, start_date, end_date, db)
    if not data:
        raise HTTPException(status_code=404, detail="No data found for the given period")
    return data