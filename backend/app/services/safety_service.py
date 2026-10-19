
import re


URGENT_SYMPTOMS = {
    "severe bleeding": [
        "severe bleeding",
        "heavy bleeding that won't stop",
        "soaking a pad every hour",
        "soaking through a pad every hour",
        "uncontrolled vaginal bleeding",
    ],
    "severe abdominal or pelvic pain": [
        "severe abdominal pain",
        "severe pelvic pain",
        "sudden severe pelvic pain",
        "unbearable period pain",
    ],
    "fainting or loss of consciousness": [
        "fainted",
        "fainting",
        "passed out",
        "loss of consciousness",
    ],
    "breathing difficulty": [
        "difficulty breathing",
        "trouble breathing",
        "shortness of breath",
        "can't breathe",
        "cannot breathe",
    ],
}


def detect_urgent_symptoms(message: str) -> list[str]:
    """Return categories of urgent warning phrases found in a message."""
    normalized = re.sub(r"\s+", " ", message.lower()).strip()

    detected = []

    for category, phrases in URGENT_SYMPTOMS.items():
        for phrase in phrases:
            pattern = rf"(?<!\w){re.escape(phrase)}(?!\w)"

            if re.search(pattern, normalized):
                detected.append(category)
                break

    return detected
