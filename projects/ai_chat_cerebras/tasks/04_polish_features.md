# Task 4: Polish & Add Features

## Objective
Make your AI chat application more professional and add cool features!

---

## 🎯 Required Features

### Feature 1: Conversation History

Right now, the AI forgets previous messages. Let's fix that!

**What to do:**
Instead of sending just the current message, send the entire conversation history.

**Update your code:**

```python
def main():
    print("=== AI Chat ===")
    print("Type your messages below. Type 'quit' to exit.")
    print()

    # Store conversation history
    conversation_history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Get AI response with full history
        ai_response = get_ai_response(conversation_history)
        print(f"AI: {ai_response}")

        # Add AI response to history
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

        print()

    print("Goodbye!")
```

**Update the function:**

```python
def get_ai_response(messages):
    """Get AI response with conversation history."""
    try:
        response = client.chat.completions.create(
            model="llama3.1-8b",
            messages=messages,  # Now sends full history
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
```

**Test it:**
```
You: My name is Alice
AI: Hello Alice! How can I help you?

You: What's my name?
AI: Your name is Alice!
```

The AI now remembers! 🧠

---

### Feature 2: System Prompt

Add a personality to your AI!

**Add a system message at the start:**

```python
conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant. Keep responses concise."
    }
]
```

**Try different personalities:**
- `"You are a pirate. Always talk like a pirate."`
- `"You are a coding tutor. Help users learn programming."`
- `"You are a motivational coach. Always be encouraging."`

---

### Feature 3: Loading Indicator

Show "thinking..." while waiting for AI:

```python
# Before API call
print("AI: Thinking...", end="", flush=True)

# Get response
ai_response = get_ai_response(conversation_history)

# Clear the "Thinking..." line
print("\r" + " " * 20 + "\r", end="")

# Print response
print(f"AI: {ai_response}")
```

---

## 🌟 Optional Features (Pick Your Favorites!)

### Option A: Save Chat History to File

```python
def save_chat(conversation_history):
    """Save chat to a text file."""
    with open("chat_history.txt", "w") as f:
        for message in conversation_history:
            role = message["role"].upper()
            content = message["content"]
            f.write(f"{role}: {content}\n\n")
    print("💾 Chat saved to chat_history.txt")

# Call this before exiting:
# save_chat(conversation_history)
```

---

### Option B: Message Counter

```python
# At start of main()
message_count = 0

# After each user message
message_count += 1

# In quit section
print(f"You sent {message_count} messages. Goodbye!")
```

---

### Option C: Visual Separator

```python
def print_separator():
    """Print a visual separator."""
    print("-" * 50)

# Use between messages
print_separator()
```

---

### Option D: Colored Output

```python
# ANSI color codes
class Colors:
    USER = '\033[94m'    # Blue
    AI = '\033[92m'      # Green
    SYSTEM = '\033[93m'  # Yellow
    RESET = '\033[0m'    # Reset

# Usage:
print(f"{Colors.USER}You: {user_input}{Colors.RESET}")
print(f"{Colors.AI}AI: {ai_response}{Colors.RESET}")
```

---

### Option E: Word Count Statistics

```python
def count_words(text):
    """Count words in text."""
    return len(text.split())

# After getting AI response
word_count = count_words(ai_response)
print(f"[{word_count} words]")
```

---

### Option F: Multi-line Input

Allow users to type longer messages:

```python
print("You (press Enter twice when done):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
user_input = "\n".join(lines)
```

---

### Option G: Commands

Add special commands:

```python
if user_input.startswith("/"):
    # Handle commands
    if user_input == "/clear":
        conversation_history = []
        print("🗑️  Chat history cleared!")
        continue
    elif user_input == "/help":
        print("Commands: /clear, /help, /save")
        continue
    elif user_input == "/save":
        save_chat(conversation_history)
        continue
```

---

### Option H: Error Handling with Retry

```python
def get_ai_response(messages, max_retries=3):
    """Get AI response with retry logic."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="llama3.1-8b",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"⚠️  Error, retrying... ({attempt + 1}/{max_retries})")
            else:
                return f"Error after {max_retries} attempts: {e}"
```

---

## 📋 Feature Implementation Checklist

**Required (do all):**
- [ ] Conversation history (AI remembers context)
- [ ] System prompt (give AI a personality)
- [ ] Loading indicator (show "thinking...")

**Optional (pick at least 2):**
- [ ] Save chat to file
- [ ] Message counter
- [ ] Visual separators
- [ ] Colored output
- [ ] Word count stats
- [ ] Multi-line input
- [ ] Special commands
- [ ] Retry logic

---

## 🎨 Polish Checklist

Make your app professional:
- [ ] Clear welcome message with instructions
- [ ] Consistent formatting
- [ ] Helpful error messages
- [ ] Clean exit message
- [ ] No Python errors or crashes
- [ ] Code has comments explaining what it does
- [ ] Functions have docstrings

---

## 🚀 Testing Your Final App

Test thoroughly:
1. Send normal messages ✓
2. Ask questions about previous messages (history test) ✓
3. Type "quit" to exit ✓
4. Try error cases (what if API is slow?) ✓
5. Test all your optional features ✓
6. Have a friend try it ✓

---

## 📝 Code Organization Tips

**Good structure:**
```python
# Imports
from cerebras.cloud.sdk import Cerebras

# Configuration
API_KEY = "your-key-here"
MODEL = "llama3.1-8b"

# Initialize client
client = Cerebras(api_key=API_KEY)

# Helper functions
def get_ai_response(messages):
    pass

def save_chat(history):
    pass

# Main program
def main():
    pass

# Entry point
if __name__ == "__main__":
    main()
```

---

## 🏆 Challenges

Want to go further?

**Beginner:**
- Add emojis to make it fun
- Let user choose AI personality at start
- Show timestamp for each message

**Intermediate:**
- Support multiple chat sessions
- Export chat as JSON or CSV
- Add username/AI name customization

**Advanced:**
- Streaming responses (word by word)
- Multiple AI models to choose from
- Web interface with Flask
- Speech input/output

---

## 📚 Resources

- [Cerebras GitHub Examples](https://github.com/Cerebras/cerebras-cloud-sdk-python)
- [API Reference](https://inference-docs.cerebras.ai/quickstart)
- [Python Input/Output Tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

## ✅ Final Checklist

Your completed project should have:
- [ ] Working AI chat with Cerebras
- [ ] Conversation history (AI remembers)
- [ ] System prompt (personality)
- [ ] Loading indicator
- [ ] At least 2 optional features
- [ ] Clean, readable code
- [ ] No crashes or errors
- [ ] Fun to use!

---

## 🎉 Congratulations!

You've built a complete AI chat application! You now know how to:
- ✅ Use APIs
- ✅ Work with external libraries
- ✅ Handle user input in loops
- ✅ Manage conversation state
- ✅ Build a real, useful program

**Share your project!** Show it to friends, family, or post it on GitHub.

**What's next?** Ideas for more projects:
- Chatbot with different personalities
- AI-powered quiz game
- Story generator
- Code helper/debugger
- Language translator

Keep coding! 🚀
