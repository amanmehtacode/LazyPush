import os
from groq import Groq
import sys

# Initialize the Groq client with the provided API key
client = Groq(api_key="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")

def get_commit_message(changes: str) -> str:
    # Create a chat completion request
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a senior software developer. Generate a detailed commit message based on the following changes."
            },
            {
                "role": "user",
                "content": changes
            }
        ],
        model="llama3-8b-8192",  # Use the provided model
    )
    # Extract and return the response content
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    # Read changes from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 groq_client.py <changes>")
        sys.exit(1)

    changes = sys.argv[1]
    commit_message = get_commit_message(changes)
    print(f"Suggested commit message: {commit_message}")