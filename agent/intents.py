def detect_intent(message: str):
    msg = message.lower()

    keywords = {
        "high_intent": {"buy", "purchase", "pricing", "demo", "interested"},
        "support": {"help", "issue", "problem", "support"},
        "general": {"how", "what", "features"}
    }

    for intent, words in keywords.items():
        if any(word in msg for word in words):
            return intent

    return "general"
