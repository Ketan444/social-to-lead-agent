import re
from agent.intents import detect_intent


def extract_lead_info(user_input):
    parts = [p.strip() for p in user_input.split(",")]

    name = parts[0] if len(parts) > 0 else None
    email = None
    platform = None

    email_match = re.search(r'[\w\.-]+@[\w\.-]+', user_input)
    if email_match:
        email = email_match.group(0)

    platforms = {"instagram", "linkedin", "twitter", "facebook", "website"}
    for word in user_input.lower().split():
        if word.strip(",") in platforms:
            platform = word.strip(",")

    return name, email, platform


def handle_message(user_input, state):
    intent = detect_intent(user_input)

    if intent == "high_intent":
        state["intent"] = "high_intent"
        return "Great! Please share your name, email, and preferred platform."

    if state.get("intent") == "high_intent":
        name, email, platform = extract_lead_info(user_input)

        if name:
            state["lead"]["name"] = name
        if email:
            state["lead"]["email"] = email
        if platform:
            state["lead"]["platform"] = platform

        missing = [
            key for key, value in state["lead"].items()
            if not value
        ]

        if missing:
            return f"Please provide your {', '.join(missing)}."

        return (
            f"Thanks {state['lead']['name']}! "
            f"We have captured your details:\n"
            f"📧 {state['lead']['email']}\n"
            f"📱 {state['lead']['platform']}\n"
            f"Our team will contact you shortly."
        )

    return "How can I help you today?"