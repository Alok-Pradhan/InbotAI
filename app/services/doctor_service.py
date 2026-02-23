class DoctorService:

    doctors = {
        "dr sharma": {
            "name": "Dr Sharma",
            "slots": [
                "monday 10am",
                "monday 11am",
                "wednesday 2pm"
            ]
        },
        "dr meena": {
            "name": "Dr Meena",
            "slots": [
                "tuesday 11am",
                "friday 1pm"
            ]
        },
        "dr timophy": {
            "name": "Dr Temophy",
            "slots": [
                "tuesday 11am",
                "friday 1pm"
            ]
        },
        "dr roman": {
            "name": "Dr Romam",
            "slots": [
                "tuesday 11am",
                "friday 1pm"
            ]
        },
        "dr preety": {
            "name": "Dr Preety",
            "slots": [
                "tuesday 11am",
                "friday 1pm"
            ]
        }
    }

    @staticmethod
    def get_doctor(key: str):
        return DoctorService.doctors.get(key.lower())

    @staticmethod
    def is_slot_available(key: str, slot: str):
        doctor = DoctorService.get_doctor(key)
        if not doctor:
            return False
        return slot.lower() in doctor["slots"]
