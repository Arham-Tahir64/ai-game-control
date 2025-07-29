import multiprocessing
from ultralytics import YOLO 

def main():
    # 1) Load the pretrained YOLOv8 model
    model = YOLO('yolov8n.pt')

    # 2) Train
    model.train(
        data='set/data.yaml',    
        epochs=100,              # 100 epochs
        imgsz=640,               # input image size
        batch=8,                 # batch size
        device=0,                # GPU
        workers=0,               
        name='bo6_enemy_local'   # run name
    )

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
