import cv2
import mss
import numpy as np
from ultralytics import YOLO
import time
import os


# Load model
model = YOLO('runs/detect/bo6_enemy_local11/weights/best.pt')

# Capture live gameplay
def capture_screen(monitor_index=2):
    with mss.mss() as sct:
        mon = sct.monitors[monitor_index]
        img = np.array(sct.grab(mon))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

# Convert fram cv2 compatible
def process_frame(frame):
    results = model(frame, imgsz=640, verbose=False)[0]
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        cls  = int(box.cls[0].item())
        label = model.names[cls]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    return frame

def main():
    GAME_MON = 2    # Monitor number to display

    cv2.namedWindow('Live Detections', cv2.WINDOW_NORMAL)

    # 15 fps
    target_fps = 15
    delay      = 1.0 / target_fps

    # Main loop
    while True:
        start = time.time()
        frame = capture_screen(GAME_MON)
        annotated = process_frame(frame)
        cv2.imshow('Live Detections', annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        elapsed = time.time() - start
        if elapsed < delay:
            time.sleep(delay - elapsed)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
