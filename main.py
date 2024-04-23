# app/main.py
from fastapi import FastAPI
import crud
from routers import appointment
from routers import doctor 
from routers import patient

app = FastAPI()

app.include_router(patient.router, prefix="/api")
app.include_router(doctor.router, prefix="/api")
app.include_router(appointment.router, prefix="/api")

# Include the CRUD operations
patients_db = crud.patients_db
doctors_db = crud.doctors_db
appointments_db = crud.appointments_db
