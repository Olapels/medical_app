
from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.patient import Patient

router = APIRouter()

patients_db = []

@router.post("/patients/", response_model=Patient)
def create_patient(patient: Patient):
    patients_db.append(patient)
    return patient


