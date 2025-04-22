from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import os

Base = declarative_base()
engine = create_engine("sqlite:///results.db")
Session = sessionmaker(bind=engine)

class DetectionResult(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    person_count = Column(Integer)
    image_path = Column(String)

def init_db():
    """Khởi tạo cơ sở dữ liệu"""
    Base.metadata.create_all(engine)

def save_result(person_count, image_path):
    """Lưu kết quả vào cơ sở dữ liệu"""
    session = Session()
    result = DetectionResult(person_count=person_count, image_path=image_path)
    session.add(result)
    session.commit()
    session.close()

def get_results(search: str = "", limit: int = 8, offset: int = 0):
    """Lấy danh sách các kết quả từ cơ sở dữ liệu với các tham số tìm kiếm và phân trang"""
    session = Session()
    query = session.query(DetectionResult)
    if search:
        query = query.filter(DetectionResult.image_path.contains(search))
    total = query.count()
    results = query.order_by(DetectionResult.timestamp.desc()).offset(offset).limit(limit).all()
    session.close()
    return results, total

def delete_old_results(days: int = 30):
    """Xóa các bản ghi cũ trong cơ sở dữ liệu (cũ hơn 30 ngày)"""
    session = Session()
    cutoff_time = datetime.now() - timedelta(days=days)
    session.query(DetectionResult).filter(DetectionResult.timestamp < cutoff_time).delete()
    session.commit()
    session.close()

def delete_old_images(directory: str, days: int = 30):
    """Xóa các ảnh cũ trong thư mục (cũ hơn 30 ngày)"""
    cutoff_time = datetime.now() - timedelta(days=days)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff_time.timestamp():
            os.remove(file_path)
            print(f"Deleted old image: {file_path}")

# Hàm xóa cả kết quả và ảnh cũ
def delete_old_data_and_images(days: int = 30, image_directory: str = "results"):
    delete_old_results(days)
    delete_old_images(image_directory, days)

def clear_all_results():
    session = Session()
    session.query(DetectionResult).delete()
    session.commit()
    session.close()