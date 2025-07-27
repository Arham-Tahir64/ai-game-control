from capture.screenshot import capture_screen
import time
import cv2

print("Starting screen capture... Press Ctrl+C to stop.")
try:
    while True:
        frame = capture_screen(show_preview=True)
        time.sleep(2)  # capture every 2 seconds

except KeyboardInterrupt:
    print("\nStopped.")
    cv2.destroyAllWindows()