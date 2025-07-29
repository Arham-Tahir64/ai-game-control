import cv2
import pytesseract
import re

def extract_ammo_count(frame):
    # Crop to the bottom right ammo HUD
    ammo_crop = frame[602:635, 940:990]

    # Convert to grayscale
    gray = cv2.cvtColor(ammo_crop, cv2.COLOR_BGR2GRAY)

    # Resize to help OCR
    resized = cv2.resize(gray, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)

    # Threshold to improve contrast
    _, thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY_INV)

    # OCR configuration (only digits)
    config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    ocr_result = pytesseract.image_to_string(thresh, config=config)

    # Extract digits
    match = re.search(r'\d+', ocr_result)
    if match:
        ammo = int(match.group())
        return ammo
    else:
        return None
