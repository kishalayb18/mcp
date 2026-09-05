#!/usr/bin/env python3
"""
Task 3: Making Your First API Call
Understand EVERY part of the chat completion call.
"""

import openai
import os

# Initialize client
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# ==========================================
# UNDERSTANDING THE API CALL STRUCTURE
# ==========================================
#
# To make an API call, you MUST provide:
# 1. model - Which AI model to use (required)
# 2. messages - Your conversation with the AI (required)
#
# The messages parameter is a list of dictionaries, each with:
# - role: Who is speaking ("user", "assistant", or "system")
# - content: What they are saying
# ==========================================

# TODO: Read each line below carefully to understand what it does
# Then uncomment ALL lines (remove the # symbols) and fill in the blanks:

response = client.chat.completions.create(
    model="gpt-5-mini",  # TODO: Use "openai/gpt-5-mini" - which AI model to use
    messages=[
        {
            "role": "user",     # TODO: Use "user" - you're the user speaking
            "content": "Hello AI, give me basics of py"   # TODO: Use "Hello AI, please introduce yourself" - your message
        }
    ]
)

# ==========================================
# REAL RESPONSE OBJECT STRUCTURE
# This is an ACTUAL response from OpenAI:
# ==========================================
"""
ChatCompletion(
    id='gen-1758773976-Ek9OxTgdgkP4Mo3ub6qf',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            message=ChatCompletionMessage(
                content="Hello! I'm ChatGPT, an AI language model created by OpenAI. I'm here to help with a wide range of tasks such as answering questions, providing explanations, generating creative content, assisting with writing, and much more. How can I assist you today?",
                role='assistant'
            )
        )
    ],
    created=1758773976,
    model='openai/gpt-5-mini',
    object='chat.completion',
    usage=CompletionUsage(
        completion_tokens=55,
        prompt_tokens=13,
        total_tokens=68
    )
)
"""

# Once you uncomment and run the code above, this will execute:
try:
    if 'response' in locals() and response:
        # The AI's text is at: response.choices[0].message.content
        ai_text = response.choices[0].message.content

        print(f"- API Key: {os.getenv('OPENAI_API_KEY')}")
        print(f"- Base URL: {os.getenv('OPENAI_API_BASE')}")
        print("✅ API Call Successful!")
        # print(f"\n🤖 AI said: {ai_text}")
        print(f"\n📊 Total tokens used: {response.usage.total_tokens}")

        # Create marker
        os.makedirs("/root/markers", exist_ok=True)
        with open("/root/markers/task3_api_call_complete.txt", "w") as f:
            f.write("SUCCESS")
    else: 
        print("\n📚 Required parameters:")
        print("1. model: 'openai/gpt-5-mini'")
        print("2. messages: [{'role': 'user', 'content': 'your message'}]")
except NameError: 
    print("\n📚 Required values:")
    print("   - model: 'openai/gpt-5-mini'")
    print("   - role: 'user'")
    print("   - content: 'Hello AI, please introduce yourself'")



# API Key: sk-s2tmRqgKqtK4RvlEeOgmtA
# - Base URL: https://api.ai.kodekloud.com
# python3 /root/code/task_3_api_call_explained.py

# https://api.ai.kodekloud.com
# sk-ewlG5Ude3br8iv2UyY7n9g
# gpt-5.4-nano


# ==========================================
# THE MAGIC PATH TO THE AI'S ANSWER
# ==========================================
#
# After making an API call, the AI's text is ALWAYS at:
# response.choices[0].message.content
#
# Let's understand each part:
# ┌─────────┐     response: The complete response object from OpenAI
# │response │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .choices: List of possible responses (usually just one)
# │.choices │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     [0]: Get the first (and typically only) choice
# │  [0]    │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .message: The message object containing the response
# │.message │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The actual text string from the AI!
# │.content │
# └─────────┘
# ==========================================



# What Are Tokens?
# Tokens are pieces of words that AI uses 
# to process text:

# Simple words = 1 token ("cat", "run")
# Complex words = multiple tokens ("unbelievable" = ~3 tokens)
# Rough estimate: 1 token ≈ 4 characters
# Average: 1 token ≈ 0.75 words
# 📊 The Three Token Types
# prompt_tokens: Your question (what you send)
# completion_tokens: AI's answer (what you get back)
# total_tokens: Sum of both (what you pay for)
# Find them in: response.usage

# 💸 Why Tokens = Money
# AI companies charge by tokens consumed:

# Input tokens: $0.80 per million ($0.0008/1K)
# Output tokens: $3.20 per million ($0.0032/1K)
# Notice: Output costs 4x more than input!

# input_tokens = response.usage.prompt_tokens    
# output_tokens = response.usage.completion_tokens   
# total_tokens = response.usage.total_tokens  


