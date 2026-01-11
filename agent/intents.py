def detect_intent(user_message: str) -> str:
    text = user_message.lower()

    # High intent FIRST
    if any(phrase in text for phrase in [
        "want to try",
        "want to subscribe",
        "i want to",
        "sign up",
        "buy",
        "try the pro"
    ]):
        return "high_intent"

    # Pricing / product questions
    if any(word in text for word in [
        "price",
        "pricing",
        "plan",
        "cost"
    ]):
        return "product_query"

    # Greeting
    if any(word in text for word in [
        "hi",
        "hello",
        "hey"
    ]):
        return "greeting"

    return "general"
