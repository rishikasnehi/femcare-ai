
from fastapi import FastAPI

app = FastAPI(
    title="FemCare AI API",
    description="Backend API for the FemCare AI women's health education chatbot",
    version="0.1.0",
)


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
