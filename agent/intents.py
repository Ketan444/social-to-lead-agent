def detect_intent(user_message: str) -> str:
    text = user_message.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "plan", "cost", "feature"]):
        return "product_query"

    if any(word in text for word in ["buy", "subscribe", "sign up", "start", "trial"]):
        return "high_intent"

    return "general"
