
from fastapi import APIRouter, HTTPException
from typing import List
from schema.appointment import Appointment

router = APIRouter()

appointments_db = []

@router.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: Appointment):
    appointments_db.append(appointment)
    return appointment




