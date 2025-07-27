from capture.screenshot import capture_screen
from vision.flash_detector import detect_red_flash
from vision.ocr_engine import extract_text_from_frame

frame = capture_screen()

flash = detect_red_flash(frame)
ocr = extract_text_from_frame(frame)

print(f"[OCR] {ocr}")
print(f"[Flash] {flash}")
