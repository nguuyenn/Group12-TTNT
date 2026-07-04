from pathlib import Path

import cv2
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "model" / "best.pt"

# Load YOLO model một lần khi import file để tránh load lại nhiều lần khi xử lý từng ảnh/frame.
model = YOLO(str(MODEL_PATH))


def detect_and_draw(frame, conf=0.5):
    # Chạy YOLO trên frame đầu vào với ngưỡng confidence mặc định là 0.5.
    results = model(frame, conf=conf)

    # Lấy tọa độ các bounding box theo format: x1, y1, x2, y2.
    boxes = results[0].boxes.xyxy

    # Copy frame để vẽ khung, tránh sửa trực tiếp ảnh gốc khi chưa cần.
    annotated_frame = frame.copy()
    plate_images = []

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)

        # Vẽ khung màu xanh quanh vùng biển số được phát hiện.
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Crop vùng biển số từ frame gốc để đưa sang OCR.
        crop = frame[y1:y2, x1:x2]
        if crop.size > 0:
            plate_images.append(crop)

    # Trả về frame đã vẽ khung và danh sách ảnh crop biển số.
    return annotated_frame, plate_images
