import cv2
from vision.ocr_engine import extract_ammo_count
from vision.flash_detector import detect_red_flash

# Load test screenshot
image_path = "test_images/cod_ss4.png"
frame = cv2.imread(image_path)

# Debug image size
print("Image size:", frame.shape)


# Run OCR
ocr_result = extract_ammo_count(frame)
print("\n🧠 OCR Result:")
print(ocr_result)

# Run red flash detection
flash_score = detect_red_flash(frame)
print("\n🚨 Red Flash Level:")
print(flash_score)
