def build_game_prompt(ammo, flash_level, event=None, time="Unknown"):
    return f"""
[Game Snapshot]

🧠 Time: {time}
🔫 Ammo in gun: {ammo}
🚨 Red Flash Level: {flash_level}
💀 Event: {event or "None"}

🎯 Summarize what likely just happened in the game in one line.
"""
