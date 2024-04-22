# app/main.py
from fastapi import FastAPI
from . import crud
from routers import appointments
from routers import doctors 
from routers import patients

app = FastAPI()

app.include_router(patient.router, prefix="/api")
app.include_router(doctor.router, prefix="/api")
app.include_router(appointment.router, prefix="/api")

# Include the CRUD operations
patients_db = crud.patients_db
doctors_db = crud.doctors_db
appointments_db = crud.appointments_db
