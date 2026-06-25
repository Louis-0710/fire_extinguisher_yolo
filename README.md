# Fire Extinguisher Detection

本專題使用 YOLO 建立一套元智大學校園滅火器即時偵測系統。系統可以透過攝影機即時讀取影像，並在畫面中框出偵測到的滅火器位置。

## Project Goal

本專題目標是建立一個具有實用價值的智慧校園物件偵測應用。透過自行拍攝元智大學校園中的滅火器影像，建立自製資料集並進行標註，再使用 YOLO 模型進行訓練，最後使用電腦攝影機進行即時偵測展示。

## Features

* 使用 YOLO 進行滅火器物件偵測
* 使用 OpenCV 讀取攝影機畫面
* 支援即時偵測並顯示 bounding box
* 使用自製校園滅火器資料集訓練
* 使用 LabelImg 進行 YOLO 格式標註

## Environment

本專題使用以下環境：

* Windows 11
* Python 3.x
* Ultralytics YOLO
* OpenCV
* LabelImg

## Installation

請先安裝 Python，接著在專案資料夾中安裝所需套件：

```bash
pip install -r requirements.txt
```

如果沒有 `requirements.txt`，也可以直接安裝：

```bash
pip install ultralytics opencv-python labelImg
```

## Dataset

本專題資料集由本人自行拍攝，圖片來源為元智大學校園環境。

資料集內容包含：

* 有滅火器的校園影像
* 無滅火器的背景影像
* 不同距離、角度與光線條件下的滅火器圖片
* 容易造成誤判的背景，例如走廊、牆壁、消防箱、紅色物品等

標註工具使用 LabelImg，標註格式為 YOLO format。

本專題只有一個偵測類別：

```txt
fire_extinguisher
```

YOLO 標籤格式如下：

```txt
class_id x_center y_center width height
```

其中 `class_id` 為 `0`，代表 `fire_extinguisher`。

## Download Links

由於完整資料集、模型權重與展示影片檔案較大，因此使用雲端連結提供。

* Full Dataset: 請貼上完整資料集 Google Drive 連結
* Trained Model best.pt: 請貼上 best.pt Google Drive 連結
* Demo Video: 請貼上展示影片 Google Drive 或 YouTube 連結

## Project Structure

```txt
fire_extinguisher_yolo/
│
├── README.md
├── requirements.txt
├── train.py
├── detect_camera.py
├── split_dataset.py
├── predict_images.py
├── predefined_classes.txt
│
├── dataset/
│   └── data.yaml
│
├── sample_dataset/
│   ├── raw_images/
│   └── raw_labels/
│
└── result/
    ├── result_close.jpg
    ├── result_far.jpg
    ├── result_angle.jpg
    └── result_background.jpg
```

說明：

* `train.py`：訓練 YOLO 模型
* `detect_camera.py`：使用攝影機進行即時偵測
* `split_dataset.py`：將資料集切分為 train / val
* `predict_images.py`：使用訓練好的模型測試驗證圖片
* `dataset/data.yaml`：YOLO 資料集設定檔
* `sample_dataset/`：放置少量範例圖片與標註檔
* `result/`：放置偵測結果截圖

## Dataset Preparation

完整資料集下載後，請將資料放成以下結構：

```txt
dataset/
│
├── raw_images/
│   ├── img_0001.jpg
│   ├── img_0002.jpg
│   └── ...
│
├── raw_labels/
│   ├── img_0001.txt
│   ├── img_0002.txt
│   └── ...
│
└── data.yaml
```

接著執行：

```bash
python split_dataset.py
```

程式會將資料切分成：

```txt
dataset/images/train
dataset/images/val
dataset/labels/train
dataset/labels/val
```

## data.yaml Example

`dataset/data.yaml` 內容如下：

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: fire_extinguisher
```

若使用絕對路徑，請依照自己的電腦路徑修改 `path`。

## Training

執行以下指令開始訓練：

```bash
python train.py
```

`train.py` 會載入 YOLO 預訓練模型，並使用自製滅火器資料集進行訓練。

訓練完成後，模型權重會儲存在：

```txt
runs/detect/fire_extinguisher_yolo/weights/best.pt
```

## Image Prediction

若要使用驗證圖片測試模型，可以執行：

```bash
python predict_images.py
```

預測結果會輸出至：

```txt
runs/detect/predict/
```

或依執行次數輸出至：

```txt
runs/detect/predict2/
runs/detect/predict3/
```

## Real-time Detection

執行以下指令啟動攝影機即時偵測：

```bash
python detect_camera.py
```

程式會開啟攝影機畫面，並使用訓練好的 YOLO 模型偵測滅火器。

按下 `q` 可以結束程式。

## Results

本系統可在攝影機畫面中偵測滅火器，並以 bounding box 標示其位置。

測試情境包含：

* 近距離滅火器偵測
* 遠距離滅火器偵測
* 斜角滅火器偵測
* 無滅火器背景測試

測試結果顯示，系統在近距離與光線充足的情況下較容易穩定偵測滅火器；在遠距離、斜角或背景較複雜的情況下，可能出現漏偵測或誤判。


