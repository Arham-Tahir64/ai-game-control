import mss
import numpy as np
import cv2
import time

def capture_screen(monitor_index=2):
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_index]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return frame

def live_preview(interval_seconds=1):
    print("screenshot every 1 seconds. ESC to exit.")

    while True:
        frame = capture_screen()
        cv2.imshow("Screen Preview", frame)

        # Wait every 2 seconds or ESC key
        key = cv2.waitKey(interval_seconds * 1000) & 0xFF
        if key == 27:  # ESC
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_preview()
