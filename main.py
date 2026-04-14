from agent.memory import create_state
from agent.graph import handle_message
from agent.test_workflow import AutomatedTestingWorkflow


def run_chatbot():
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


def run_testing_tool():
    workflow = AutomatedTestingWorkflow()
    result = workflow.run("sample_data/sample_large_testing_data.csv")
    print(result)


if __name__ == "__main__":
    mode = input("Choose mode (chat/test): ").lower()

    if mode == "chat":
        run_chatbot()
    elif mode == "test":
        run_testing_tool()
    else:
        print("Invalid mode selected")