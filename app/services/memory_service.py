class MemoryService:

    conversations = {}

    @staticmethod
    def add_message(patient_id: str, role: str, content: str):
        if patient_id not in MemoryService.conversations:
            MemoryService.conversations[patient_id] = []

        MemoryService.conversations[patient_id].append({
            "role": role,
            "content": content
        })

        # keep last 6 messages only (limit memory size)
        MemoryService.conversations[patient_id] = \
            MemoryService.conversations[patient_id][-6:]

    @staticmethod
    def get_history(patient_id: str):
        return MemoryService.conversations.get(patient_id, [])
