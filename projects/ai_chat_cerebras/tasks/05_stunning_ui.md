# Task 5: Build a Stunning UI

## Objective
Transform your terminal chat app into a **beautiful web interface** with a modern, professional look! 🎨

---

## Why Add a UI?

**Terminal App:**
```
You: Hello
AI: Hi there!
```
✓ Works
✗ Not shareable
✗ Looks basic

**Web App:**
- ✨ Beautiful, modern design
- 🌐 Shareable via browser
- 📱 Works on mobile
- 🎨 Professional appearance
- 👥 Impress friends/teachers

---

## What You're Building

A web-based chat interface that looks like ChatGPT, Claude, or other modern AI chat apps!

**Features:**
- Chat bubbles for messages
- User avatar on right, AI on left
- Input box at bottom
- Smooth scrolling
- Clean, modern design
- Runs in web browser

---

## Tool: Streamlit

We'll use **Streamlit** - a Python library that makes beautiful web apps with just a few lines of code!

**Why Streamlit?**
- ✅ Easy to learn (easier than HTML/CSS)
- ✅ Beautiful by default
- ✅ Perfect for AI apps
- ✅ Built-in chat components
- ✅ Just Python - no JavaScript needed!

---

## Step 1: Install Streamlit

```bash
pip install streamlit
```

Test it works:
```bash
streamlit hello
```

A browser window should open with a demo app! 🎉

---

## Step 2: Create Your UI File

Create a new file called `chat_ui.py`:

```python
import streamlit as st
from cerebras.cloud.sdk import Cerebras

# Page configuration
st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chat Assistant")
st.caption("Powered by Cerebras")

# Initialize Cerebras client
client = Cerebras(api_key="your-api-key-here")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

# Display chat messages
for message in st.session_state.messages:
    # Skip system messages in display
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama3.1-8b",
                messages=st.session_state.messages,
                max_tokens=500,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content
            st.markdown(ai_response)

    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
```

---

## Step 3: Run Your App

```bash
streamlit run chat_ui.py
```

**Your browser will open with a beautiful chat interface!** 🚀

---

## Understanding the Code

### Page Configuration
```python
st.set_page_config(
    page_title="AI Chat",     # Browser tab title
    page_icon="🤖",           # Browser tab icon
    layout="centered"         # Layout style
)
```

### Session State (Memory)
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

**Why?** Streamlit reruns your script on every interaction. `session_state` keeps data between reruns.

### Chat Message Display
```python
with st.chat_message("user"):
    st.markdown("Hello!")
```

Creates a chat bubble with user avatar.

### Chat Input
```python
if prompt := st.chat_input("Type here..."):
    # User submitted a message
```

The `:=` is a walrus operator - assigns AND checks in one line.

### Spinner (Loading)
```python
with st.spinner("Thinking..."):
    # API call here
```

Shows a loading animation while AI thinks.

---

## Customization Options

### 1. Change Theme Colors

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

**Dark mode:** Above colors
**Light mode:** Change backgroundColor to "#FFFFFF"

---

### 2. Add Custom Avatars

```python
with st.chat_message("user", avatar="👤"):
    st.markdown(message)

with st.chat_message("assistant", avatar="🤖"):
    st.markdown(response)
```

Try: 😊, 👨‍💻, 🧑‍🎓, 🦾, 🌟

---

### 3. Add Sidebar Controls

```python
with st.sidebar:
    st.title("⚙️ Settings")

    # Temperature slider
    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    # Model selector
    model = st.selectbox(
        "Model",
        ["llama3.1-8b", "llama3.1-70b"]
    )

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
```

---

### 4. Add System Prompt Editor

```python
with st.sidebar:
    st.subheader("🎭 AI Personality")

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant.",
        height=100
    )

    # Update system message
    st.session_state.messages[0]["content"] = system_prompt
```

---

### 5. Download Chat History

```python
with st.sidebar:
    if st.button("💾 Download Chat"):
        chat_text = ""
        for msg in st.session_state.messages:
            if msg["role"] != "system":
                chat_text += f"{msg['role'].upper()}: {msg['content']}\n\n"

        st.download_button(
            "Download as TXT",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )
```

---

### 6. Message Statistics

```python
with st.sidebar:
    st.metric(
        "Messages Sent",
        len([m for m in st.session_state.messages if m["role"] == "user"])
    )
```

---

### 7. Streaming Responses (Advanced)

Make AI type word-by-word like ChatGPT:

```python
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""

    # Stream the response
    for chunk in client.chat.completions.create(
        model="llama3.1-8b",
        messages=st.session_state.messages,
        stream=True
    ):
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(full_response)
```

---

## Complete Enhanced Version

Here's a full-featured version:

```python
import streamlit as st
from cerebras.cloud.sdk import Cerebras

# Page config
st.set_page_config(
    page_title="AI Chat Pro",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")

    api_key = st.text_input("API Key", type="password", value="your-key-here")

    temperature = st.slider("Creativity", 0.0, 1.0, 0.7, 0.1)

    model = st.selectbox("Model", ["llama3.1-8b", "llama3.1-70b"])

    system_prompt = st.text_area(
        "System Prompt",
        "You are a helpful AI assistant.",
        height=100
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [{
            "role": "system",
            "content": system_prompt
        }]
        st.rerun()

    st.divider()

    # Stats
    if "messages" in st.session_state:
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.metric("Messages Sent", user_msgs)

# Main area
st.title("🤖 AI Chat Pro")
st.caption("Powered by Cerebras | Ultra-fast AI inference")

# Initialize
client = Cerebras(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": system_prompt
    }]

# Display messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=st.session_state.messages,
                    max_tokens=500,
                    temperature=temperature
                )
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })
            except Exception as e:
                st.error(f"Error: {e}")
```

---

## Deployment Options

### Option 1: Share Locally

```bash
streamlit run chat_ui.py
```

Share URL: `http://localhost:8501`
Others on same WiFi can access it!

### Option 2: Deploy to Cloud (Free!)

**Streamlit Community Cloud:**
1. Push code to GitHub
2. Go to streamlit.io/cloud
3. Connect GitHub repo
4. Deploy!
5. Get shareable URL: `your-app.streamlit.app`

---

## Comparison: Before vs After

| Feature | Terminal (Tasks 1-4) | Web UI (Task 5) |
|---------|---------------------|-----------------|
| Look | Basic text | Beautiful chat bubbles |
| Share | No | Yes - send URL |
| Mobile | No | Yes - responsive |
| Customization | Limited | Themes, colors, fonts |
| Professional | Prototype | Production-ready |

---

## Testing Checklist

- [ ] App runs without errors
- [ ] Messages display correctly
- [ ] AI responds to input
- [ ] Chat history persists
- [ ] Sidebar controls work
- [ ] Looks good on mobile
- [ ] No console errors

---

## Extra Challenges

**Beginner:**
- Add emoji reactions to messages
- Add message timestamps
- Add dark/light mode toggle

**Intermediate:**
- Add file upload (chat about uploaded files)
- Add voice input button
- Export chat as PDF

**Advanced:**
- Multi-session support (multiple conversations)
- User authentication
- Share conversation via link
- Real-time collaboration (multiple users)

---

## Troubleshooting

**Port already in use:**
```bash
streamlit run chat_ui.py --server.port 8502
```

**App won't load:**
- Check your API key is correct
- Make sure Cerebras SDK is installed
- Check terminal for error messages

**Messages not persisting:**
- Make sure you're using `st.session_state`
- Don't reset session_state unnecessarily

---

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Chat Elements](https://docs.streamlit.io/library/api-reference/chat)
- [Streamlit Gallery](https://streamlit.io/gallery) - Examples
- [Deploy to Cloud](https://streamlit.io/cloud)

---

## ✅ Final Checklist

Your completed UI should have:
- [ ] Beautiful web interface
- [ ] Working chat functionality
- [ ] Sidebar with settings
- [ ] Customized theme/colors
- [ ] At least 2 extra features
- [ ] Mobile responsive
- [ ] Ready to share!

---

## 🎉 Congratulations!

You've built a **complete, production-ready AI chat application** with:
- ✅ Real AI integration (Cerebras)
- ✅ Conversation memory
- ✅ Beautiful web UI
- ✅ Professional features
- ✅ Shareable online

**You can now:**
- Add it to your portfolio
- Share with friends/family
- Deploy it online
- Customize it further
- Build other AI apps!

**This is a real skill** - you now know how to build AI-powered web applications! 🚀

---

## What's Next?

Ideas for your next project:
- **AI Tutor** - Subject-specific help
- **Story Generator** - Creative writing assistant
- **Code Helper** - Programming mentor
- **Language Translator** - Multi-language chat
- **Image Chat** - Add image analysis (multimodal)

Keep building! The sky's the limit! 🌟
