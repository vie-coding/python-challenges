# Task 1: Setup Cerebras API

## Objective
Get your Cerebras API key so you can build an AI chat application.

---

## What is Cerebras?
Cerebras is a company that provides super-fast AI inference (running AI models). They offer a free tier with **1 million tokens per day** - perfect for learning!

---

## Steps to Get Your API Key

### Step 1: Create an Account
1. Go to **https://cloud.cerebras.ai/**
2. Click **Sign Up** or **Get Started**
3. Sign up using:
   - Email
   - Google account
   - GitHub account
4. **No credit card required** for the free tier!

### Step 2: Navigate to API Keys
1. After logging in, you'll see the dashboard
2. Look for **"API Keys"** in the menu (usually on the left sidebar or top navigation)
3. Click on **API Keys**

### Step 3: Generate Your API Key
1. Click **"Create API Key"** or **"Generate New Key"**
2. Give it a name (e.g., "My Chat Project")
3. Click **Generate** or **Create**
4. Your API key will appear - it looks like: `csk-xxxxxxxxxxxxxxxxxxxxx`

### Step 4: Save Your API Key
⚠️ **IMPORTANT:** Copy and save your API key immediately!
- You won't be able to see it again after closing the window
- Keep it secret - don't share it or commit it to GitHub

**Save it in a safe place:**
- Write it in a text file temporarily
- Or keep the browser tab open while you work

---

## Install Required Python Package

Open your terminal/command prompt and run:

```bash
pip install cerebras-cloud-sdk
```

This installs the official Cerebras Python library.

---

## Test Your API Key

Create a file called `test_api.py` and paste this code:

```python
from cerebras.cloud.sdk import Cerebras

# Replace 'your-api-key-here' with your actual API key
client = Cerebras(api_key="your-api-key-here")

# Test the API
response = client.chat.completions.create(
    model="llama3.1-8b",
    messages=[
        {"role": "user", "content": "Say hello!"}
    ]
)

print(response.choices[0].message.content)
```

Run it:
```bash
python test_api.py
```

If you see the AI respond with "Hello!" or similar, **you're ready to go!** ✅

---

## Troubleshooting

**Error: "Invalid API key"**
- Double-check you copied the entire key
- Make sure there are no extra spaces
- Verify the key on cloud.cerebras.ai

**Error: "Module not found: cerebras"**
- Run `pip install cerebras-cloud-sdk` again
- Make sure you're using Python 3.8 or higher

**Error: Rate limit exceeded**
- You've used your daily 1M tokens
- Wait until tomorrow or upgrade to paid tier

---

## Resources

- [Cerebras Cloud Dashboard](https://cloud.cerebras.ai/)
- [Cerebras Python SDK Documentation](https://github.com/Cerebras/cerebras-cloud-sdk-python)
- [QuickStart Guide](https://inference-docs.cerebras.ai/quickstart)

---

## ✅ Checkpoint

Before moving to Task 2, make sure:
- [ ] You have a Cerebras account
- [ ] You have your API key saved
- [ ] You installed `cerebras-cloud-sdk`
- [ ] You tested the API and got a response

**Ready?** Move on to `02_basic_chat_loop.md`!
