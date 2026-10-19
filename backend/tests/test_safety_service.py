import pytest

from app.services.safety_service import detect_urgent_symptoms


@pytest.mark.parametrize(
    "message",
    [
        "I have severe bleeding.",
        "I am soaking a pad every hour.",
        "I have severe pelvic pain.",
        "I fainted earlier today.",
        "I am having difficulty breathing.",
        "I have shortness of breath.",
    ],  
)
def test_detects_urgent_symptoms(message):
    assert detect_urgent_symptoms(message)


@pytest.mark.parametrize(
    "message",
    [
        "What is PCOS?",
        "Why do I experience mild period cramps?",
        "How can I maintain menstrual health?",
        "What foods contain iron?",
    ],
)
def test_does_not_flag_ordinary_health_questions(message):
    assert detect_urgent_symptoms(message) == []
