import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 1. The Tool (Plain Python)
def get_current_weather():
    return "72°F and sunny in Boston"

# 2. The Schema (Telling the model what exists)
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Returns the current local weather."
    }
}]

# 3. Ask a question the model CANNOT know without the tool
messages = [{"role": "user", "content": "What is the weather outside?"}]

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=messages,
    tools=tools
)

# Inspect what the model emitted:
print(response)
##choice = response.choices[0].message
#print("Tool Calls Requested by Model:")
#print(choice.tool_calls)