from fastapi import APIRouter
from pydantic import BaseModel
from app.services.appointment_service import AppointmentService

router = APIRouter()


class AppointmentRequest(BaseModel):
    patient_id: str
    doctor: str
    slot: str


@router.post("/book-appointment")
def book(request: AppointmentRequest):
    appointment = AppointmentService.book(
        request.patient_id,
        request.doctor,
        request.slot
    )

    return {"message": "Appointment booked", "data": appointment}
