import mss
import numpy as np
import cv2
import time

def capture_screen(monitor_index=1, show_preview=False):
    # Captures screen and returns a BGR image in order to use with OpenCV
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_index]  # use monitor_index=1 for primary screen
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)  # raw BGRA image
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        if show_preview:
            cv2.imshow("Live Screen", frame)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
        
        return frame
