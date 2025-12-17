# Task 3: Connect to Cerebras API

## Objective
Replace the placeholder AI response with **real AI responses** from Cerebras!

---

## What You're Building

Now we'll make the AI actually work by:
1. Importing the Cerebras SDK
2. Creating a client with your API key
3. Sending user messages to the AI
4. Displaying real AI responses

---

## Step 1: Import and Setup

At the top of your `chat.py` file, add:

```python
from cerebras.cloud.sdk import Cerebras

# Initialize Cerebras client
# Replace 'your-api-key-here' with your actual API key from Task 1
client = Cerebras(api_key="your-api-key-here")
```

⚠️ **Important:** Replace `"your-api-key-here"` with your actual API key!

---

## Step 2: Create the AI Response Function

Add this function before your `main()` function:

```python
def get_ai_response(user_message):
    """
    Send a message to Cerebras AI and get a response.

    Args:
        user_message (str): The message from the user

    Returns:
        str: The AI's response
    """
    try:
        # Make API call to Cerebras
        response = client.chat.completions.create(
            model="llama3.1-8b",  # The AI model to use
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,  # Maximum length of response
            temperature=0.7  # Creativity level (0.0 to 1.0)
        )

        # Extract and return the AI's message
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
```

---

## Step 3: Update Your Chat Loop

Replace the placeholder response line with a call to your function:

```python
# OLD (remove this):
print("AI: [AI response will go here]")

# NEW (use this instead):
ai_response = get_ai_response(user_input)
print(f"AI: {ai_response}")
```

---

## Complete Code Structure

Your `chat.py` should now look like this:

```python
from cerebras.cloud.sdk import Cerebras

# Initialize Cerebras client
client = Cerebras(api_key="your-api-key-here")

def get_ai_response(user_message):
    """Get AI response from Cerebras."""
    try:
        response = client.chat.completions.create(
            model="llama3.1-8b",
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== AI Chat ===")
    print("Type your messages below. Type 'quit' to exit.")
    print()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        # Get real AI response
        ai_response = get_ai_response(user_input)
        print(f"AI: {ai_response}")
        print()

    print("Goodbye!")

if __name__ == "__main__":
    main()
```

---

## Step 4: Test It!

Run your program:
```bash
python chat.py
```

Try asking:
- "Hello, who are you?"
- "Tell me a joke"
- "What is Python?"
- "Write a haiku about coding"

You should see **real AI responses**! 🎉

---

## Understanding the API Call

Let's break down the important parts:

```python
response = client.chat.completions.create(
    model="llama3.1-8b",        # Which AI model to use
    messages=[                   # List of messages
        {"role": "user", "content": user_message}
    ],
    max_tokens=500,             # Max response length
    temperature=0.7             # Randomness (0=focused, 1=creative)
)
```

**Parameters explained:**
- `model`: The AI brain to use (llama3.1-8b is fast and good)
- `messages`: List of conversation messages
- `max_tokens`: Limits response length (prevents very long answers)
- `temperature`: Controls creativity
  - 0.0 = Very focused and deterministic
  - 0.7 = Balanced (recommended)
  - 1.0 = Very creative and random

---

## Troubleshooting

**Error: "Invalid API key"**
- Check your API key is correct
- Make sure there are no extra spaces
- Verify it's surrounded by quotes

**Error: "Name 'client' is not defined"**
- Make sure `client = Cerebras(...)` is outside the function
- Check it's at the top of your file

**Error: "Rate limit exceeded"**
- You've used your free daily limit (1M tokens)
- Wait until tomorrow or upgrade your account

**AI gives weird responses:**
- Try adjusting `temperature` (lower = more focused)
- Check your prompt is clear
- Make sure `max_tokens` isn't too low

**Slow responses:**
- This is normal! AI takes a few seconds to think
- Cerebras is actually very fast compared to others

---

## Testing Checklist

- [ ] Program starts without errors
- [ ] AI gives real, relevant responses
- [ ] Multiple messages work in a row
- [ ] "quit" still exits properly
- [ ] No crashes or Python errors

---

## Understanding API Costs

With the free tier:
- You get **1 million tokens per day**
- A token ≈ 4 characters (roughly)
- "Hello, how are you?" ≈ 5 tokens
- You can send thousands of messages per day

---

## Resources

- [Cerebras Python SDK](https://github.com/Cerebras/cerebras-cloud-sdk-python)
- [API Documentation](https://inference-docs.cerebras.ai/quickstart)
- [Available Models](https://inference-docs.cerebras.ai/quickstart)

---

## ✅ Checkpoint

Before moving to Task 4, verify:
- [ ] Your API key is working
- [ ] AI responds to your messages
- [ ] Responses make sense
- [ ] No errors in the console

**Congratulations!** You've built a working AI chat application!

**Ready to make it better?** Move on to `04_polish_features.md`!
