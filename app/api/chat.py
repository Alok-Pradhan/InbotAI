from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import RAGService
from app.services.llm_service import LLMService
from app.services.patient_service import PatientService
from app.services.appointment_service import AppointmentService
from app.services.doctor_service import DoctorService
from app.services.memory_service import MemoryService


router = APIRouter()

rag = RAGService()
llm = LLMService()


class ChatRequest(BaseModel):
    message: str
    patient_id: str | None = None


@router.post("/chat")
def chat(request: ChatRequest):

    message = request.message.lower()

    # ===============================
    # 1️⃣ REPORT CHECK
    # ===============================
    if "report" in message and request.patient_id:

        patient = PatientService.get_patient(request.patient_id)

        if not patient:
            return {"response": "Patient not found."}

        reports = patient.get("reports", [])

        if not reports:
            return {"response": "You have no reports available."}

        return {"response": f"Your reports: {', '.join(reports)}"}

    # ===============================
    # 2️⃣ SMART BOOKING LOGIC
    # ===============================
    if "book" in message and request.patient_id:

        # Detect doctor
        if "sharma" in message:
            doctor_key = "dr sharma"
        elif "meena" in message:
            doctor_key = "dr meena"
        else:
            return {"response": "Please specify doctor name."}

        # Detect slot
        possible_slots = [
            "monday 10am",
            "monday 11am",
            "wednesday 2pm",
            "tuesday 11am",
            "friday 1pm"
        ]

        slot = None
        for ps in possible_slots:
            if ps in message:
                slot = ps
                break

        if not slot:
            return {"response": "Please specify available slot clearly."}

        # Validate availability
        if not DoctorService.is_slot_available(doctor_key, slot):
            return {"response": "Selected slot is not available."}

        doctor = DoctorService.get_doctor(doctor_key)

        appointment = AppointmentService.book(
            request.patient_id,
            doctor["name"],
            slot
        )

        return {
            "response": f"Appointment booked successfully with {doctor['name']} at {slot}."
        }

    # ===============================
    # 3️⃣ GENERAL RAG + PATIENT CONTEXT
    # ===============================

    patient_context = ""

    if request.patient_id:
        patient = PatientService.get_patient(request.patient_id)
        if patient:
            patient_context = f"""
            Patient Name: {patient['name']}
            Reports: {', '.join(patient['reports']) if patient['reports'] else 'None'}
            Medicines: {', '.join(patient['medicines']) if patient['medicines'] else 'None'}
            """

    context = rag.retrieve(request.message)

    final_context = context + "\n\n" + patient_context

    history = []

    if request.patient_id:
        history = MemoryService.get_history(request.patient_id)

    answer = llm.generate(final_context, request.message, history)

    # Save conversation
    if request.patient_id:
        MemoryService.add_message(request.patient_id, "user", request.message)
        MemoryService.add_message(request.patient_id, "assistant", answer)

    return {"response": answer}