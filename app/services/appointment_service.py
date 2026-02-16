import json
from uuid import uuid4

DATA_PATH = "app/data/appointments.json"


class AppointmentService:

    @staticmethod
    def _read():
        with open(DATA_PATH, "r") as f:
            return json.load(f)

    @staticmethod
    def _write(data):
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def book(patient_id: str, doctor: str, slot: str):
        appointments = AppointmentService._read()

        new_appointment = {
            "id": str(uuid4()),
            "patient_id": patient_id,
            "doctor": doctor,
            "slot": slot,
            "status": "Booked"
        }

        appointments.append(new_appointment)
        AppointmentService._write(appointments)

        return new_appointment
