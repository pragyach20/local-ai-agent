import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Create Gemini AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.3
)

# Store conversation history
conversation_history = []


def run_agent(user_input):
    """Send a request to the AI agent and return its response."""

    conversation_history.append(
        f"User: {user_input}"
    )

    conversation = "\n".join(conversation_history)

    prompt = f"""
You are a helpful local AI assistant.

Conversation history:
{conversation}

Answer the user's latest request clearly and concisely.
Use previous conversation context when it is relevant.
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        answer = "".join(
            item.get("text", "")
            for item in response.content
            if isinstance(item, dict) and item.get("type") == "text"
        )
    else:
        answer = response.content

    conversation_history.append(
        f"Agent: {answer}"
    )

    return answer


if __name__ == "__main__":
    print("====================================")
    print("          LOCAL AI AGENT")
    print("====================================")
    print("Type 'exit' to stop the agent.")
    print("The agent remembers your conversation during the session.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        if not user_input.strip():
            continue

        try:
            answer = run_agent(user_input)
            print(f"\nAgent: {answer}\n")

        except Exception as e:
            print(f"\nError: {e}\n")