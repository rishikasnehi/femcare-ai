
from fastapi.testclient import TestClient

from app.main import app
import app.api.chat as chat_module


client = TestClient(app)


def test_unrelated_question_is_rejected(monkeypatch):
    def fake_generate_response(**kwargs):
        raise AssertionError("Gemini should not be called")

    monkeypatch.setattr(
        chat_module,
        "generate_response",
        fake_generate_response,
    )

    response = client.post(
        "/api/chat/",
        json={
            "message": "What is photosynthesis?",
            "temperature": 0.3,
        },
    )

    assert response.status_code == 200
    assert "women's health education assistant" in response.json()["reply"]


def test_urgent_symptoms_return_safety_message(monkeypatch):
    def fake_generate_response(**kwargs):
        raise AssertionError("Gemini should not be called")

    monkeypatch.setattr(
        chat_module,
        "generate_response",
        fake_generate_response,
    )

    response = client.post(
        "/api/chat/",
        json={
            "message": "I have severe pelvic pain.",
            "temperature": 0.3,
        },
    )

    assert response.status_code == 200
    assert "urgent medical attention" in response.json()["reply"]


def test_supported_question_calls_gemini(monkeypatch):
    def fake_generate_response(**kwargs):
        assert kwargs["prompt"] == "What is PCOS?"
        assert kwargs["system_instruction"]
        return "PCOS is a hormonal condition that can affect menstrual cycles."

    monkeypatch.setattr(
        chat_module,
        "generate_response",
        fake_generate_response,
    )

    response = client.post(
        "/api/chat/",
        json={
            "message": "What is PCOS?",
            "temperature": 0.3,
        },
    )

    assert response.status_code == 200
    assert "PCOS" in response.json()["reply"]


def test_empty_message_is_rejected():
    response = client.post(
        "/api/chat/",
        json={
            "message": "",
            "temperature": 0.3,
        },
    )

    assert response.status_code == 422
