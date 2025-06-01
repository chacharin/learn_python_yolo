# 🔍 Real-Time Object Detection with YOLOv8 and OpenCV

โปรเจกต์นี้สาธิตการใช้งาน YOLOv8 สำหรับตรวจจับวัตถุจากกล้อง USB แบบ real-time 
---

## 📦 Requirements

- Python >= 3.8
- OpenCV (`cv2`)
- Ultralytics YOLOv8

### 🔧 ติดตั้งไลบรารีที่จำเป็น
```bash
pip install opencv-python ultralytics
```

---

## 📂 โครงสร้างโค้ด

| ไฟล์                          | รายละเอียด |
|-------------------------------|------------|
| `camera_view.py`              | แสดงภาพจากกล้อง USB เฉย ๆ |
| `yolov8n_detection.py`        | ตรวจจับวัตถุด้วย YOLOv8n (pre-trained) |
| `custom_model_detection.py`   | ตรวจจับวัตถุด้วยโมเดลที่ฝึกเอง (`best.pt`) พร้อม confidence threshold |

---

## 🧠 คำอธิบายสำคัญ

### 🔁 `model(frame)[0]` หมายถึงอะไร?
- ฟังก์ชัน `model()` คืนค่าผลลัพธ์ในรูปแบบ **list ของ batch ทั้งหมด**
- ถึงแม้ใส่แค่ 1 ภาพ YOLOv8 จะคืน list 1 ชิ้น
- ดังนั้น `[0]` หมายถึง “ผลลัพธ์ของภาพแรกในชุด”

### 🎨 `cv2.rectangle()` อธิบาย argument
```python
cv2.rectangle(img, pt1, pt2, color, thickness)
```
| argument | ความหมาย |
|----------|-----------|
| `img` | ภาพที่ต้องการวาด |
| `pt1` | พิกัดมุมบนซ้ายของกรอบ (x1, y1) |
| `pt2` | พิกัดมุมล่างขวาของกรอบ (x2, y2) |
| `color` | สีกรอบในรูปแบบ BGR (0,255,0 คือเขียว) |
| `thickness` | ความหนาเส้น (เช่น 2 พิกเซล) |

### 🏷️ `cv2.putText()` อธิบาย argument
```python
cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
```
| argument | ความหมาย |
|----------|-----------|
| `img` | ภาพที่ต้องการใส่ข้อความ |
| `text` | ข้อความที่จะแสดง (เช่น class name) |
| `org` | ตำแหน่งเริ่มต้นของข้อความ (x, y) |
| `fontFace` | รูปแบบฟอนต์ เช่น `cv2.FONT_HERSHEY_SIMPLEX` |
| `fontScale` | ขนาดข้อความ เช่น 0.6 |
| `color` | สีข้อความ (BGR) |
| `thickness` | ความหนาเส้นตัวอักษร |

---

## ✅ การใช้งานทีละขั้น

### ▶️ 1. กล้อง (เฉย ๆ)
```bash
python camera_view.py
```

### ▶️ 2. ตรวจจับด้วย YOLOv8n
```bash
python yolov8n_detection.py
```

### ▶️ 3. ตรวจจับด้วยโมเดลฝึกเอง (วาง `best.pt` ไว้ในโฟลเดอร์เดียวกัน)
```bash
python custom_model_detection.py
```

---
