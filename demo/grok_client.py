import os
import requests
from load_env import load_env

load_env()

API_KEY = os.getenv("GROK_API_KEY")
BASE_URL = os.getenv("GROK_BASE_URL", "https://api.x.ai/v1")

def run_grok(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-4-latest",
        "messages": [
            {
                "role": "system",
                "content": "You are an enterprise AI agent. Always return valid JSON only."
            },
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        data = res.json()
    except Exception as e:
        print("⚠️ API error:", e)
        return None


    try:
        return data["choices"][0]["message"]["content"]
    except:
        print("⚠️ Unexpected response format")
        return None
