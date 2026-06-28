from agents.agent import process_request
from memory.conversation import (
    add_user_message,
    add_assistant_message,
)


def main():
    print("=" * 50)
    print("🚀 Welcome to Nexus AI")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            print("\nNexus AI: Goodbye! 👋")
            break

        try:
            add_user_message(prompt)
            answer = process_request(prompt)
            add_assistant_message(answer)
            print(f"\nNexus AI: {answer}\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()