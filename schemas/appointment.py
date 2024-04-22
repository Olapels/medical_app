# appointment pydantic model
from pydantic import BaseModel

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str
