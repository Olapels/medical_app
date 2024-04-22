# app/routers/crud.py
from fastapi import HTTPException
from typing import List
from schemas.patient import Patient
from schemas.doctor import Doctor
from schemas.appointment import Appointment

patients_db = []
doctors_db = []
appointments_db = []

def create_patient(patient: Patient):
    patients_db.append(patient)
    return patient

def read_patients():
    return patients_db

def read_patient(patient_id: int):
    for patient in patients_db:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

def update_patient(patient_id: int, patient: Patient):
    for i, p in enumerate(patients_db):
        if p.id == patient_id:
            patients_db[i] = patient
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

def delete_patient(patient_id: int):
    for i, patient in enumerate(patients_db):
        if patient.id == patient_id:
            del patients_db[i]
            return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")

def create_doctor(doctor: Doctor):
    doctors_db.append(doctor)
    return doctor

def read_doctors():
    return doctors_db

def read_doctor(doctor_id: int):
    for doctor in doctors_db:
        if doctor.id == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

def update_doctor(doctor_id: int, doctor: Doctor):
    for i, d in enumerate(doctors_db):
        if d.id == doctor_id:
            doctors_db[i] = doctor
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

def delete_doctor(doctor_id: int):
    for i, doctor in enumerate(doctors_db):
        if doctor.id == doctor_id:
            del doctors_db[i]
            return {"message": "Doctor deleted successfully"}
    raise HTTPException(status_code=404, detail="Doctor not found")

def create_appointment(appointment: Appointment):
    # Find the first available doctor
    available_doctors = [doctor for doctor in doctors_db if doctor.is_available]
    if not available_doctors:
        raise HTTPException(status_code=400, detail="No available doctors")

    doctor = available_doctors[0]
    appointment.doctor_id = doctor.id
    appointments_db.append(appointment)
    return appointment

def read_appointments():
    return appointments_db

def delete_appointment(appointment_id: int):
    for i, appointment in enumerate(appointments_db):
        if appointment.id == appointment_id:
            del appointments_db[i]
            return {"message": "Appointment deleted successfully"}
    raise HTTPException(status_code=404, detail="Appointment not found")
