import pyautogui
import time

while True:
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot_{int(time.time())}.png')
