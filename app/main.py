from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.patient import router as patient_router
from app.api.appointment import router as appointment_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(patient_router)
app.include_router(appointment_router)

@app.get("/")
def root():
    return {"message": "Hospital AI is running"}
