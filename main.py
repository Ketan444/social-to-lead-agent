from agent.memory import create_state
from agent.graph import handle_message

def main():
    state = create_state()
    print("AutoStream Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        if state["intent"] == "high_intent":
            lead = state["lead"]
            if not lead["name"]:
                lead["name"] = user_input
            elif not lead["email"]:
                lead["email"] = user_input
            elif not lead["platform"]:
                lead["platform"] = user_input

        response = handle_message(user_input, state)
        print("Bot:", response)

if __name__ == "__main__":
    main()
