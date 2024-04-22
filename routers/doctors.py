# app/routers/doctor.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.doctor import Doctor

router = APIRouter()

doctors_db = []

@router.post("/doctors/", response_model=Doctor)
def create_doctor(doctor: Doctor):
    doctors_db.append(doctor)
    return doctor


