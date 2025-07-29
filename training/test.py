import cv2
import mss
import numpy as np
from ultralytics import YOLO
import time

# import combat handler
from actions.combat import on_enemy_detected

# Load your trained model
model = YOLO('runs/detect/bo6_enemy_local11/weights/best.pt')

def capture_screen(monitor_index=2):
    with mss.mss() as sct:
        mon = sct.monitors[monitor_index]
        img = np.array(sct.grab(mon))
    # convert to BGR for OpenCV
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def process_frame(frame):
    # run detection
    results = model(frame, imgsz=640, verbose=False)[0]

    # collect Enemy detections
    enemy_boxes = []
    for box in results.boxes:
        cls_id = int(box.cls[0].item())
        label  = model.names[cls_id]
        if label == 'Enemy':
            enemy_boxes.append(box)

    # feed enemy boxes to detection function
    if enemy_boxes:
        on_enemy_detected(enemy_boxes)

    # draw all boxes
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        cls_id = int(box.cls[0].item())
        label  = model.names[cls_id]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'{label} {conf:.2f}',
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    return frame

def main():
    GAME_MON = 2  # second monitor
    cv2.namedWindow('Live Detections', cv2.WINDOW_NORMAL)

    target_fps = 15
    delay      = 1.0 / target_fps

    while True:
        start = time.time()
        frame = capture_screen(GAME_MON)
        annotated = process_frame(frame)
        cv2.imshow('Live Detections', annotated)

        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # throttle framerate
        elapsed = time.time() - start
        if elapsed < delay:
            time.sleep(delay - elapsed)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
