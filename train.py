from ultralytics import YOLO

# 載入 YOLOv8 nano 預訓練模型
model = YOLO("yolov8n.pt")

# 開始訓練
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    name="fire_extinguisher_yolo"
)