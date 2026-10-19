
from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import generate_response

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        reply = generate_response(
            prompt=request.message,
            temperature=request.temperature,
        )

        return ChatResponse(reply=reply)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail="The AI service is not configured or available.",
        ) from exc

    except Exception as exc:
        # Keep internal errors and credentials out of API responses.
        print(f"Chat API error: {type(exc).__name__}")

        raise HTTPException(
            status_code=502,
            detail="Unable to generate a response. Please try again.",
        ) from exc
