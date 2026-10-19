
from fastapi import APIRouter, HTTPException

from app.prompts.femcare_prompt import FEMCARE_SYSTEM_PROMPT
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import generate_response
from app.services.scope_service import classify_scope

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Step 1: Check whether the question is in scope
    if not classify_scope(request.message):
        return ChatResponse(
            reply=(
                "I'm FemCare AI, a women's health education assistant. "
                "I can help with menstrual health, PCOS/PCOD, breast health, "
                "mood and hormonal changes, weight and metabolic health, "
                "vaginal and reproductive health, fertility, thyroid disorders, "
                "mental well-being, anemia, pregnancy, postpartum health, "
                "menopause, and lifestyle-related health conditions. "
                "Please ask a question related to these topics."
            )
        )

    # Step 2: Generate a response only for accepted questions
    try:
        reply = generate_response(
            prompt=request.message,
            temperature=request.temperature,
            system_instruction=FEMCARE_SYSTEM_PROMPT,
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
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=502,
            detail="Unable to generate a response. Please try again.",
        ) from exc

