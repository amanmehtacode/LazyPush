import os
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

def get_commit_message(changes: str) -> str:
    # Define the commit message template
    template = """
### Summary

Provide a brief summary of the changes made.

### Details

- **Files Modified**: List the files that were modified.
- **New Features**: Describe any new features added.
- **Bug Fixes**: Describe any bugs that were fixed.
- **Improvements**: Explain any improvements or optimizations made.

### Impact

Explain the impact of the changes, including any potential effects on other parts of the application or system.

### Related Issues

Reference any related issues or tickets (if applicable).

### Example

### Summary

Enhanced user interface with improved responsiveness.

### Details

- **Files Modified**: index.html, styles.css, main.js
- **New Features**: Added a new responsive layout for the homepage.
- **Bug Fixes**: Fixed alignment issues in the navigation bar.
- **Improvements**: Optimized CSS for faster loading times.

### Impact

The changes improve the user experience by making the site more responsive and faster to load. No major changes to existing functionalities.

### Related Issues

- Issue #123: Fix navigation bar alignment
- Issue #124: Improve homepage responsiveness
    """
    
    # Create a chat completion request with the template
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a senior software developer. Use the provided template to generate a detailed commit message based on the following changes."
            },
            {
                "role": "user",
                "content": f"Template:\n{template}\n\nChanges:\n{changes}"
            }
        ],
        model="llama3-8b-8192",  # or the model you prefer
    )
    
    # Extract and return the response content
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    # Example changes, replace this with the actual diff output in your use case
    changes = "Add sample feature to improve user experience"
    commit_message = get_commit_message(changes)
    print(f"Suggested commit message: {commit_message}")
