import cv2
import numpy as np

def detect_red_flash(frame, red_threshold=100):
    # Extract red channel
    red_channel = frame[:, :, 2]  # BGR format

    # Get average red intensity
    red_mean = np.mean(red_channel)

    # Debug
    print(f"[FlashDetector] Red mean: {red_mean:.2f}")

    if red_mean > red_threshold:
        return "HIGH"
    elif red_mean > (red_threshold * 0.75):
        return "MEDIUM"
    else:
        return "LOW"
