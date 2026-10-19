
import re


HEALTH_KEYWORDS = {
    "menstrual_health": {
        "period", "menstrual", "menstruation", "menstruate",
        "menstrual cycle", "cramps", "bleeding", "pms",
        "missed period", "irregular period", "heavy period",
        "tampon", "sanitary pad", "period pain",
    },
    "pcos_pcod": {
        "pcos", "pcod", "polycystic ovary",
        "polycystic ovarian", "insulin resistance",
        "ovarian cyst",
    },
    "breast_health": {
        "breast", "breasts", "breast cancer",
        "breast lump", "nipple", "mammogram",
    },
    "mood_and_hormones": {
        "mood swing", "mood swings", "hormone",
        "hormonal", "premenstrual", "pmdd",
    },
    "weight_and_metabolism": {
        "weight gain", "weight loss", "metabolism",
        "bloating", "water retention",
    },
    "vaginal_and_reproductive_health": {
        "vagina", "vaginal", "vulva", "vulvar",
        "vaginal discharge", "vaginal itching",
        "vaginal infection", "yeast infection",
        "reproductive health", "pelvic pain",
        "genital health",
    },
    "fertility_and_reproductive_planning": {
        "fertility", "fertile", "ovulation", "conception",
        "trying to conceive", "infertility", "contraception",
        "birth control", "family planning", "pregnancy planning",
        "fertility awareness",
    },
    "thyroid_and_hormonal_disorders": {
        "thyroid", "hypothyroidism", "hyperthyroidism",
        "thyroid disorder", "hormonal disorder",
        "hormone imbalance", "endocrine disorder",
    },
    "mental_health_and_emotional_wellbeing": {
        "mental health", "emotional well-being",
        "emotional wellbeing", "anxiety", "depression",
        "stress management", "panic attack",
        "emotional health", "mental wellbeing",
    },
    "anemia_and_nutritional_deficiencies": {
        "anemia", "anaemia", "iron deficiency",
        "iron-deficiency anemia", "hemoglobin",
        "haemoglobin", "nutritional deficiency",
        "vitamin deficiency", "vitamin b12", "folate deficiency",
    },
    "pregnancy_postpartum_and_menopause": {
        "pregnancy", "pregnant", "postpartum",
        "after childbirth", "after delivery",
        "breastfeeding", "perimenopause", "menopause",
        "menopausal", "prenatal", "postnatal",
    },
    "lifestyle_related_health": {
        "sleep", "physical activity", "exercise",
        "nutrition", "healthy diet", "sedentary lifestyle",
        "lifestyle", "hydration", "stress",
    },
}


def classify_scope(message: str) -> bool:
    """
    Return True when a supported health keyword is detected.

    This is a basic keyword filter, not a medical classifier
    or a determination that the question is medically safe.
    """
    normalized = re.sub(
        r"\s+",
        " ",
        message.lower(),
    ).strip()

    for keywords in HEALTH_KEYWORDS.values():
        for keyword in keywords:
            pattern = (
                rf"(?<!\w){re.escape(keyword)}(?!\w)"
            )

            if re.search(pattern, normalized):
                return True

    return False
