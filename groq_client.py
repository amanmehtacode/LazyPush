import os
from groq import Groq

# Initialize the Groq client with the provided API key
client = Groq(api_key="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")

def get_commit_message(changes: str) -> str:
    # Create a chat completion request
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Generate a concise commit message based on the following changes."
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
    # For demonstration, you might want to replace this with the actual diff output
    changes = "Add sample feature to improve user experience"
    commit_message = get_commit_message(changes)
    print(f"Suggested commit message: {commit_message}")
