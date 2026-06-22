import cv2
from pathlib import Path
from ultralytics import YOLO

print("程式開始執行")

model_path = Path("runs/detect/fire_extinguisher_yolo/weights/best.pt")

print("目前模型路徑：", model_path)

if not model_path.exists():
    print("找不到 best.pt，請確認模型路徑是否正確")
    input("按 Enter 結束")
    exit()

print("正在載入 YOLO 模型...")
model = YOLO(str(model_path))
print("模型載入完成")

cap = None

# 嘗試不同攝影機編號
for camera_id in [0, 1, 2, 3]:
    print(f"嘗試開啟攝影機 {camera_id} ...")
    test_cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)

    if test_cap.isOpened():
        cap = test_cap
        print(f"成功開啟攝影機 {camera_id}")
        break
    else:
        test_cap.release()

if cap is None:
    print("無法開啟任何攝影機")
    print("請確認：")
    print("1. 攝影機沒有被 LINE、Teams、Chrome、相機 App 佔用")
    print("2. Windows 已允許桌面應用程式使用攝影機")
    input("按 Enter 結束")
    exit()

print("開始即時偵測，按 q 離開")

while True:
    ret, frame = cap.read()

    if not ret:
        print("無法讀取攝影機畫面")
        break

    results = model(frame, conf=0.5)
    annotated_frame = results[0].plot()

    cv2.imshow("Fire Extinguisher Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("使用者按下 q，結束程式")
        break

cap.release()
cv2.destroyAllWindows()
print("程式結束")