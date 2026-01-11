from agent.intents import detect_intent
from agent.rag import answer_from_knowledge
from agent.tools import mock_lead_capture

def handle_message(user_input, state):

    # Detect intent only if not already set
    if state["intent"] is None:
        state["intent"] = detect_intent(user_input)

    intent = state["intent"]

    if intent == "greeting":
        state["intent"] = None
        return "Hi! I can help you with AutoStream pricing, plans, or getting started."

    if intent == "product_query":
        state["intent"] = None
        return answer_from_knowledge(user_input)

    if intent == "high_intent":
        lead = state["lead"]

        if lead["name"] is None:
            return "Great! May I know your name?"

        if lead["email"] is None:
            return "Thanks. Could you share your email?"

        if lead["platform"] is None:
            return "Which platform do you create content on? (YouTube, Instagram, etc.)"

        # All details collected → capture lead
        mock_lead_capture(
            lead["name"],
            lead["email"],
            lead["platform"]
        )

        # Reset state after successful capture
        state["intent"] = None
        state["lead"] = {"name": None, "email": None, "platform": None}

        return "Thanks! Our team will reach out to you shortly."

    state["intent"] = None
    return "Let me know how I can help you."

