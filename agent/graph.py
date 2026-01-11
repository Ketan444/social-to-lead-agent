from agent.intents import detect_intent
from agent.rag import answer_from_knowledge
from agent.tools import mock_lead_capture

def handle_message(user_input, state):

    # Detect intent only once per flow
    if state["intent"] is None:
        state["intent"] = detect_intent(user_input)

    intent = state["intent"]
    lead = state["lead"]

    # Step 1: Greeting
    if intent == "greeting":
        state["intent"] = None
        return "Sure! I can help you with our pricing plans. What would you like to know?"

    # Step 2: Knowledge Retrieval (RAG)
    if intent == "product_query":
        state["intent"] = None
        return answer_from_knowledge(user_input)

    # Step 3–5: High Intent → Lead Qualification → Tool Execution
    if intent == "high_intent":

        if lead["name"] is None:
            return "Great! May I know your name?"

        if lead["email"] is None:
            return "Thanks! Could you please share your email?"

        if lead["platform"] is None:
            return "Which platform do you create content on? (YouTube, Instagram, etc.)"

        # All required details collected
        mock_lead_capture(
            lead["name"],
            lead["email"],
            lead["platform"]
        )

        # Reset state after lead capture
        state["intent"] = None
        state["lead"] = {"name": None, "email": None, "platform": None}

        return "Thanks! Our team will reach out to you shortly."

    return "Let me know how I can help you."

