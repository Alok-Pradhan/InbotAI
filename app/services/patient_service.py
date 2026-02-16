import json
import os
from uuid import uuid4

DATA_PATH = "app/data/patients.json"


class PatientService:

    @staticmethod
    def _read():
        with open(DATA_PATH, "r") as f:
            return json.load(f)

    @staticmethod
    def _write(data):
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def register(name: str, email: str):
        patients = PatientService._read()

        new_patient = {
            "id": str(uuid4()),
            "name": name,
            "email": email,
            "reports": [],
            "medicines": []
        }

        patients.append(new_patient)
        PatientService._write(patients)

        return new_patient

    @staticmethod
    def get_patient(patient_id: str):
        patients = PatientService._read()
        for p in patients:
            if p["id"] == patient_id:
                return p
        return None
