from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.patient import router as patient_router
from app.api.appointment import router as appointment_router

app = FastAPI()

# ✅ Add CORS Middleware HERE
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(patient_router)
app.include_router(appointment_router)

@app.get("/")
def root():
    return {"message": "Hospital AI is running"}