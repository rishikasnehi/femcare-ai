
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The user's message",
    )

    temperature: float = Field(
        default=0.3,
        ge=0.0,
        le=2.0,
        description="Controls response randomness",
    )


class ChatResponse(BaseModel):
    reply: str
