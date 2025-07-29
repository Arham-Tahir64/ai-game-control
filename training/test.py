import cv2
from ultralytics import YOLO

# 1. Load model & open input
model = YOLO('runs/detect/bo6_enemy_local11/weights/best.pt')
cap   = cv2.VideoCapture('test_images/test.mp4')

# 2. Prepare VideoWriter
fps    = cap.get(cv2.CAP_PROP_FPS)
w      = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')                   # or 'XVID','H264' etc.
out    = cv2.VideoWriter('gameplay_with_detections.mp4', fourcc, fps, (w, h))

def process_frame(frame):
    results = model(frame, imgsz=640)[0]
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf   = box.conf[0].item()
        cls_id = int(box.cls[0].item())
        label  = model.names[cls_id]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    return frame

# 3. Read, process, write
while True:
    ret, frame = cap.read()
    if not ret:
        break
    annotated = process_frame(frame)
    out.write(annotated)        # write to output file

cap.release()
out.release()
print("Saved ➜ gameplay_with_detections.mp4")
