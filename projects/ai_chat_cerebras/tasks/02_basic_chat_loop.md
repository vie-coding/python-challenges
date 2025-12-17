# Task 2: Build a Basic Chat Loop

## Objective
Create a simple program that lets you type messages and the AI responds. No API yet - just the chat interface.

---

## What You're Building

A program that:
1. Asks you to type a message
2. Takes your input
3. Displays your message
4. Gives a fake AI response (for now)
5. Repeats until you type "quit"

**Example:**
```
You: Hello
AI: [This will be the AI response later]

You: How are you?
AI: [This will be the AI response later]

You: quit
Goodbye!
```

---

## Requirements

### 1. Welcome Message
When the program starts, print:
```
=== AI Chat ===
Type your messages below. Type 'quit' to exit.
```

### 2. Chat Loop
Use a `while` loop to keep the conversation going:
- Prompt the user for input with `"You: "`
- If they type "quit" (case-insensitive), break the loop
- Otherwise, print a placeholder AI response

### 3. Placeholder Response
For now, the AI response can be a simple placeholder like:
```
AI: [AI response will go here]
```

### 4. Exit Message
When the user quits, print:
```
Goodbye!
```

---

## Code Template

Create a file called `chat.py`:

```python
def main():
    # Print welcome message
    print("=== AI Chat ===")
    print("Type your messages below. Type 'quit' to exit.")
    print()

    # Main chat loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to quit
        # TODO: Add quit check here

        # Display placeholder AI response
        # TODO: Add AI response here

        print()  # Empty line for readability

    # Exit message
    print("Goodbye!")

if __name__ == "__main__":
    main()
```

---

## Your Tasks

1. **Complete the quit check**
   - Check if `user_input.lower() == "quit"`
   - If yes, `break` out of the loop

2. **Add the placeholder response**
   - Print `"AI: [AI response will go here]"`

3. **Test your program**
   - Run it multiple times
   - Type several messages
   - Make sure "quit" exits properly
   - Try "QUIT" and "Quit" (should all work)

---

## Testing Checklist

Run your program and verify:
- [ ] Welcome message displays
- [ ] You can type a message
- [ ] Placeholder AI response appears
- [ ] You can send multiple messages
- [ ] Typing "quit" exits the program
- [ ] Typing "QUIT" or "Quit" also exits
- [ ] "Goodbye!" message displays on exit

---

## Extra Challenge (Optional)

Make it fancier:
- Add a line separator between messages (`print("-" * 40)`)
- Add color to the text (look up ANSI color codes)
- Count how many messages were sent
- Add a typing indicator (print "AI is thinking..." before response)

---

## Example Output

```
=== AI Chat ===
Type your messages below. Type 'quit' to exit.

You: Hello there
AI: [AI response will go here]

You: What's the weather?
AI: [AI response will go here]

You: quit
Goodbye!
```

---

## Troubleshooting

**Loop doesn't stop:**
- Check your quit condition
- Make sure you're using `.lower()` for case-insensitive comparison
- Verify you're using `break` correctly

**Nothing prints:**
- Check your indentation
- Make sure print statements are inside the loop

---

## ✅ Checkpoint

Before moving to Task 3, make sure:
- [ ] Your chat loop works
- [ ] "quit" exits the program
- [ ] Messages display correctly
- [ ] Your code is clean and readable

**Ready?** Move on to `03_api_integration.md` where we'll connect to Cerebras!
