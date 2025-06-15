from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a:float, b:float) -> str:
    """Useful for performing basic arithmetic operations"""
    return f"The result of {a} + {b} is {a+b}"



def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0)

    tools = [calculator]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or answer questions.")

    while True:
        user_input = input("\nYou: ").strip() #strip() removes whitespace from the beginning and end of the string

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()