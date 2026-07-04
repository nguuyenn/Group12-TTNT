import cv2

from utils.detector import detect_and_draw
from utils.file_utils import get_output_video_path, save_frame_image, save_plate_image
from utils.ocr_reader import read_plate_text


VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".mkv")


def process_input(input_path):
    # Điều hướng xử lý dựa trên đuôi file: video thì xử lý video, còn lại xem như ảnh.
    if input_path.lower().endswith(VIDEO_EXTENSIONS):
        process_video(input_path)
    else:
        process_image(input_path)


def process_image(image_path):
    # Đọc ảnh từ đường dẫn người dùng nhập vào.
    frame = cv2.imread(image_path)
    if frame is None:
        print("Không thể đọc ảnh.")
        return

    # Phát hiện biển số, vẽ khung lên ảnh, đồng thời lấy ra các vùng ảnh biển số.
    frame, plates = detect_and_draw(frame)

    for plate in plates:
        # Lưu từng ảnh crop biển số, sau đó đưa ảnh đó vào OCR để đọc ký tự.
        plate_path = save_plate_image(plate)
        text = read_plate_text(plate)
        print(f"Biển số: {text} | Ảnh: {plate_path}")

    # Lưu ảnh kết quả đã được vẽ khung nhận diện.
    frame_path = save_frame_image(frame)
    print(f"Ảnh kết quả đã lưu tại: {frame_path}")

    # Hiển thị ảnh bằng OpenCV. Nhấn phím bất kỳ để đóng cửa sổ.
    cv2.imshow("Ket qua nhan dien", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_video(video_path):
    # Mở video đầu vào bằng OpenCV.
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Không thể mở video.")
        return

    # Lấy thông tin video để tạo file video output cùng kích thước và FPS.
    output_video_path = get_output_video_path()
    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(
        str(output_video_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )
    if not out.isOpened():
        cap.release()
        print("Không thể tạo video output.")
        return

    while True:
        # Đọc từng frame trong video. Khi hết frame thì dừng vòng lặp.
        ret, frame = cap.read()
        if not ret:
            break

        # Xử lý nhận diện biển số trên frame hiện tại.
        frame, plates = detect_and_draw(frame)

        for plate in plates:
            # Lưu ảnh biển số và đọc text bằng OCR.
            save_plate_image(plate)
            text = read_plate_text(plate)
            if text:
                # Ghi text OCR lên frame video để dễ quan sát kết quả.
                cv2.putText(
                    frame,
                    text,
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )

        # Ghi frame đã xử lý vào video output.
        out.write(frame)

        # Hiển thị video realtime. Nhấn q để dừng sớm.
        cv2.imshow("Video - Nhan dien bien so", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Giải phóng tài nguyên sau khi xử lý xong.
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video đã lưu tại: {output_video_path}")


if __name__ == "__main__":
    path = input("Nhập đường dẫn ảnh hoặc video: ").strip()
    process_input(path)
