
import pytest

from app.services.scope_service import classify_scope


@pytest.mark.parametrize(
    "message",
    [
        "Why do I experience cramps during my period?",
        "What is PCOS?",
        "What should I know about a breast lump?",
        "Why do I experience mood swings?",
        "What can cause unexplained weight gain?",
        "What causes vaginal itching?",
        "How does ovulation affect fertility?",
        "What is hypothyroidism?",
        "How can I manage anxiety?",
        "What are the symptoms of iron deficiency?",
        "What is postpartum recovery?",
        "How does sleep affect women's health?",
    ],
)
def test_supported_health_topics(message):
    assert classify_scope(message) is True


@pytest.mark.parametrize(
    "message",
    [
        # Programming and technology
        "Write a C++ program for binary search.",
        "Explain the working of a computer network.",
        "Build a React login page.",
        "How does artificial intelligence work?",

        # Mathematics and science
        "Explain the Pythagorean theorem.",
        "What is Newton's second law of motion?",
        "Explain photosynthesis.",

        # History, politics, and geography
        "Who was the first Prime Minister of India?",
        "Explain the causes of World War II.",
        "What is the capital of Japan?",

        # Business, finance, and economics
        "How does the stock market work?",
        "Explain the concept of compound interest.",
        "How do I start a small business?",

        # Education and careers
        "Help me prepare for a coding interview.",
        "Write an essay about climate change.",
        "How can I improve my resume?",

        # Entertainment, sports, and general knowledge
        "Recommend some Bollywood movies.",
        "Who won the last cricket World Cup?",
        "Tell me a joke.",

        # Everyday non-health questions
        "Suggest a recipe for paneer butter masala.",
        "What should I wear to a party?",
        "Plan a three-day trip to Goa.",
    ],
)
def test_unrelated_topics(message):
    assert classify_scope(message) is False
