# project-AI-Group12

Dự án nhận diện biển số xe sử dụng YOLOv8 để phát hiện vùng biển số và EasyOCR để nhận dạng ký tự.

## Chức năng chính

- Nhận diện biển số xe từ ảnh.
- Nhận diện biển số xe từ video.
- Vẽ khung nhận diện quanh vùng biển số.
- Cắt và lưu riêng ảnh biển số đã phát hiện.
- Đọc ký tự biển số bằng EasyOCR.
- Lưu ảnh hoặc video sau khi xử lý.

## Công nghệ sử dụng

- Python
- OpenCV
- YOLOv8 / Ultralytics
- EasyOCR
- PyTorch

## Cấu trúc thư mục

```text
TTNT/
│
├── app.py                    # File chính để chạy chương trình
│
├── model/
│   └── best.pt               # Mô hình YOLOv8 đã huấn luyện
│
├── utils/
│   ├── detector.py           # Phát hiện biển số bằng YOLOv8
│   ├── ocr_reader.py         # Nhận dạng ký tự bằng EasyOCR
│   └── file_utils.py         # Xử lý đường dẫn và lưu file kết quả
│
├── static/
│   ├── outputs/              # Lưu ảnh/video sau xử lý
│   └── plates/               # Lưu ảnh biển số đã cắt
│
└── requirements.txt          # Danh sách thư viện cần cài đặt
```

## Cài đặt

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows:

```bash
.venv\Scripts\activate
```

Cài đặt thư viện:

```bash
pip install -r TTNT/requirements.txt
```

## Cách chạy chương trình

Di chuyển vào thư mục `TTNT`:

```bash
cd TTNT
```

Chạy chương trình:

```bash
python app.py
```

Sau đó nhập đường dẫn ảnh hoặc video cần nhận diện.

Ví dụ:

```text
Nhap duong dan anh hoac video: D:\data\car.jpg
```

## Kết quả đầu ra

- Ảnh biển số đã cắt được lưu tại `TTNT/static/plates`.
- Ảnh hoặc video sau xử lý được lưu tại `TTNT/static/outputs`.
- Ký tự biển số nhận dạng được sẽ được in ra màn hình terminal.

## Hạn chế hiện tại

- Chưa có giao diện người dùng hoàn chỉnh.
- Chưa hỗ trợ nhận diện trực tiếp từ webcam.
- Kết quả OCR có thể sai khi ảnh bị mờ, thiếu sáng, lóa hoặc biển số bị nghiêng nhiều.

## Hướng phát triển

- Bổ sung chức năng nhận diện từ webcam.
- Xây dựng giao diện web bằng Flask hoặc Streamlit.
- Tối ưu tiền xử lý ảnh để cải thiện kết quả OCR.
- Lưu lịch sử nhận diện vào cơ sở dữ liệu.
- Tối ưu tốc độ xử lý khi chạy với video.
