# camera_view.py
# โปรแกรมพื้นฐานสำหรับมือใหม่ ใช้เปิดกล้อง USB และแสดงภาพแบบ real-time ด้วย OpenCV

import cv2  # ไลบรารีสำหรับจัดการภาพ/วิดีโอ

# 🎥 เปิดกล้อง (index 0 หมายถึงกล้องตัวแรกของระบบ เช่น webcam)
cap = cv2.VideoCapture(0)

# 🛠️ ตั้งค่าความละเอียดของกล้อง
# CAP_PROP_FRAME_WIDTH: ความกว้างของเฟรมภาพ (หน่วย: พิกเซล)
# CAP_PROP_FRAME_HEIGHT: ความสูงของเฟรมภาพ (หน่วย: พิกเซล)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("✅ กล้องเปิดสำเร็จ - กด 'q' เพื่อออก")

while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()

    # ถ้าไม่สำเร็จ (ret == False) ให้ออก
    if not ret:
        print("❌ ไม่สามารถอ่านภาพจากกล้องได้")
        break

    # แสดงผลภาพ
    cv2.imshow("Live Camera Feed", frame)

    # รอ 1 มิลลิวินาที และตรวจสอบว่ามีการกดปุ่ม 'q' หรือไม่
    # cv2.waitKey(1): รอ 1 ms / & 0xFF: ตรวจสอบคีย์จริง / ord('q'): ตรวจสอบคีย์ q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการเชื่อมต่อกล้องและหน้าต่างแสดงภาพ
cap.release()
cv2.destroyAllWindows()
