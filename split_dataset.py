import random
import shutil
from pathlib import Path

raw_images_dir = Path("dataset/raw_images")
raw_labels_dir = Path("dataset/raw_labels")

train_img_dir = Path("dataset/images/train")
val_img_dir = Path("dataset/images/val")
train_label_dir = Path("dataset/labels/train")
val_label_dir = Path("dataset/labels/val")

# 清空舊的 train / val，避免之前殘留檔案影響訓練
for d in [train_img_dir, val_img_dir, train_label_dir, val_label_dir]:
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True, exist_ok=True)

image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

image_files = [
    p for p in raw_images_dir.iterdir()
    if p.is_file() and p.suffix.lower() in image_exts
]

image_files = sorted(image_files, key=lambda p: p.name)

random.seed(42)
random.shuffle(image_files)

train_ratio = 0.8
train_count = int(len(image_files) * train_ratio)

train_files = image_files[:train_count]
val_files = image_files[train_count:]

def copy_group(files, target_img_dir, target_label_dir):
    for img_path in files:
        label_path = raw_labels_dir / f"{img_path.stem}.txt"

        shutil.copy2(img_path, target_img_dir / img_path.name)

        target_label_path = target_label_dir / f"{img_path.stem}.txt"

        if label_path.exists():
            shutil.copy2(label_path, target_label_path)
        else:
            # 沒有滅火器的圖片，建立空白標籤
            target_label_path.write_text("", encoding="utf-8")

copy_group(train_files, train_img_dir, train_label_dir)
copy_group(val_files, val_img_dir, val_label_dir)

print("資料切分完成")
print("總圖片數：", len(image_files))
print("訓練集：", len(train_files))
print("驗證集：", len(val_files))
print("沒有標註的圖片會自動產生空白 txt，代表背景圖片")