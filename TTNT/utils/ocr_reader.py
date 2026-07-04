import cv2
import easyocr


# Tạo EasyOCR reader một lần để tránh khởi tạo lại model OCR nhiều lần.
reader = easyocr.Reader(["en"])


def read_plate_text(image):
    # Hàm này nhận được cả đường dẫn ảnh hoặc ảnh OpenCV array.
    if isinstance(image, str):
        image = cv2.imread(image)

    # Nếu ảnh không đọc được hoặc crop lỗi thì trả chuỗi rỗng để app không crash.
    if image is None:
        return ""

    # EasyOCR thường đọc ổn hơn khi ảnh biển số được chuyển sang grayscale.
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # readtext trả về danh sách kết quả gồm bbox, text, confidence.
    results = reader.readtext(image)
    text_parts = []
    for _, text_found, _ in results:
        text_parts.append(text_found)

    # Ghép các phần text OCR đọc được thành một chuỗi biển số.
    return " ".join(text_parts).strip()
