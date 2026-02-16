from fastapi import APIRouter
from pydantic import BaseModel
from app.services.patient_service import PatientService

router = APIRouter()


class RegisterRequest(BaseModel):
    name: str
    email: str


@router.post("/register")
def register(request: RegisterRequest):
    patient = PatientService.register(request.name, request.email)
    return {"message": "Patient registered", "data": patient}
