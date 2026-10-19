
from fastapi import FastAPI

from app.api.chat import router as chat_router

app = FastAPI(
    title="FemCare AI API",
    description="Backend API for the FemCare AI women's health education chatbot",
    version="0.2.0",
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to FemCare AI API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
