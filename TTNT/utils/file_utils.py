from pathlib import Path

import cv2


BASE_DIR = Path(__file__).resolve().parents[1]
STATIC_DIR = BASE_DIR / "static"
PLATE_DIR = STATIC_DIR / "plates"
OUTPUT_DIR = STATIC_DIR / "outputs"


def _next_file_path(folder, prefix, suffix):
    # Đảm bảo thư mục tồn tại trước khi ghi file.
    folder.mkdir(parents=True, exist_ok=True)

    # Đặt tên tăng dần để không ghi đè ảnh cũ: plate_0001.jpg, plate_0002.jpg...
    index = len(list(folder.glob(f"{prefix}_*{suffix}"))) + 1
    return folder / f"{prefix}_{index:04d}{suffix}"


def save_plate_image(plate):
    # Lưu ảnh crop biển số vào thư mục static/plates.
    file_path = _next_file_path(PLATE_DIR, "plate", ".jpg")
    cv2.imwrite(str(file_path), plate)
    return file_path


def save_frame_image(frame):
    # Lưu ảnh kết quả đã vẽ bounding box vào thư mục static/outputs.
    file_path = _next_file_path(OUTPUT_DIR, "frame", ".jpg")
    cv2.imwrite(str(file_path), frame)
    return file_path


def get_output_video_path():
    # Trả về đường dẫn video output và đảm bảo thư mục outputs đã tồn tại.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR / "output_video.mp4"
