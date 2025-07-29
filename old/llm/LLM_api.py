import requests

def query_lm_studio(prompt):
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",  # LM Studio OpenAI-compatible endpoint
        headers={"Content-Type": "application/json"},
        json={
            "model": "phi-3-mini-4k-instruct",  # or whatever name is shown in LM Studio
            "messages": [
                {"role": "system", "content": "You are a game AI assistant that summarizes key events."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.6,
            "max_tokens": 100
        }
    )
    return response.json()["choices"][0]["message"]["content"]
