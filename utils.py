# import os
# import uuid
# from database.models import Detection

# def save_image(uploaded_file):
#     folder = "static/images"
#     os.makedirs(folder, exist_ok=True)
#     file_ext = uploaded_file.name.split('.')[-1]
#     file_name = f"{uuid.uuid4()}.{file_ext}"
#     file_path = os.path.join(folder, file_name)
    
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     return file_path


# def load_history(db, filter_count=0):
#     return db.query(Detection).filter(Detection.count >= filter_count).order_by(Detection.timestamp.desc()).all()

import os
from datetime import datetime

def save_uploaded_file(uploaded_file, save_dir="images"):
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(save_dir, f"{timestamp}_{uploaded_file.name}")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
