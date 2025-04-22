# from ultralytics import YOLO
# import cv2

# model = YOLO('yolov8n.pt')

# def detect_people(image_path):
#     results = model(image_path)
#     img = results[0].plot()  # Bounding boxes
#     count = sum(1 for c in results[0].boxes.cls if int(c) == 0)  # class 0 = person
#     output_path = image_path.replace("static/images/", "static/images/result_")
#     cv2.imwrite(output_path, img)
#     return output_path, count

# from ultralytics import YOLO
# import cv2
# import os
# from datetime import datetime

# model = YOLO("yolov8n.pt")

# def detect_person(image_path: str, output_path: str) -> tuple:
#     results = model(image_path)
#     result = results[0]
#     boxes = result.boxes
#     img = cv2.imread(image_path)

#     person_count = 0
#     for box in boxes:
#         cls = int(box.cls[0])
#         if model.names[cls] == "person":
#             person_count += 1
#             xyxy = box.xyxy[0].cpu().numpy().astype(int)
#             cv2.rectangle(img, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)

#     filename = os.path.basename(image_path)
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     output_filename = f"{timestamp}_{filename}"
#     output_file = os.path.join(output_path, output_filename)

#     cv2.imwrite(output_file, img)
#     return person_count, output_file

# from ultralytics import YOLO
# import cv2
# import os
# from datetime import datetime
# from pathlib import Path

# model = YOLO("yolov8n.pt")

# def detect_person(image_path: str, output_path: str) -> tuple:
#     results = model(image_path)
#     result = results[0]
#     boxes = result.boxes
#     img = cv2.imread(image_path)

#     person_count = 0
#     for box in boxes:
#         cls = int(box.cls[0])
#         conf = float(box.conf[0])  # Độ chính xác
#         label = model.names[cls]

#         if label == "person":
#             person_count += 1
#             xyxy = box.xyxy[0].cpu().numpy().astype(int)
#             x1, y1, x2, y2 = xyxy

#             # Vẽ khung
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

#             # Thêm nhãn và độ chính xác
#             text = f"{label} {conf:.2f}"
#             cv2.putText(img, text, (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#     os.makedirs(output_path, exist_ok=True)

#     filename = os.path.basename(image_path)
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     output_filename = f"{timestamp}_{filename}"
#     output_file = os.path.join(output_path, output_filename)

#     cv2.imwrite(output_file, img)

#     return person_count, str(Path(output_file).as_posix())

from ultralytics import YOLO
import cv2
import numpy as np
import os
from datetime import datetime
from pathlib import Path
from PIL import Image

model = YOLO("yolov8n.pt")

def detect_person(file, output_path: str) -> tuple:
    # Đọc ảnh từ file upload (in-memory)
    img = Image.open(file).convert("RGB")
    img_np = np.array(img)

    results = model(img_np)
    result = results[0]
    boxes = result.boxes

    person_count = 0
    for box in boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]

        if label == "person":
            person_count += 1
            xyxy = box.xyxy[0].cpu().numpy().astype(int)
            x1, y1, x2, y2 = xyxy
            cv2.rectangle(img_np, (x1, y1), (x2, y2), (0, 0, 255), 2)
            text = f"{label} {conf:.2f}"
            cv2.putText(img_np, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)

    os.makedirs(output_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.basename(file.name)
    name_without_ext = os.path.splitext(filename)[0]
    
    output_filename = f"{name_without_ext}_{timestamp}_detected.png"
    output_file = os.path.join(output_path, output_filename)

    # Lưu kết quả
    cv2.imwrite(output_file, cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))

    return person_count, str(Path(output_file).as_posix())



