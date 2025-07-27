import requests
from vision.flash_detector import detect_red_flash
from vision.ocr_engine import extract_ammo_count
import cv2

frame = cv2.imread("cod_ss4.png")
ammo = extract_ammo_count(frame)
flash_level = detect_red_flash(frame)
kill_count = 2
caption = "Walking around"

# LM Studio API endpoint
url = "http://127.0.0.1:1234/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "model": "phi-3-mini-4k-instruct",
    "messages": [
        {
            "role": "system",
            "content": "You are a game event classifier. Based on game signals, decide if the player is currently in COMBAT or NO_COMBAT. Only reply with 'combat' or 'no_combat'."
        },
        {
            "role": "user",
            "content": f"""
Flash level: {flash_level}
Current ammo: {ammo}
Kills this second: {kill_count}
Scene description: {caption}

Is the player currently in combat or not? Respond only with: combat or no_combat.
"""
        }
    ],
    "temperature": 0.1 
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

# Extract result
classification = data["choices"][0]["message"]["content"].strip().lower()
print("🧠 Combat status:", classification)

# Basic Spotify logic hook
def combat_status(classification):
    if classification == "combat":
        return True
    elif classification == "no_combat":
        return False
