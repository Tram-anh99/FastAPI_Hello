from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <--- 1. NHỚ IMPORT DÒNG NÀY

# --- PHẦN 1: CẤU HÌNH DATABASE (SQLAlchemy) ---
# Bạn thay: user, password, localhost, dbname bằng thông tin thật của bạn
URL_DATABASE = "postgresql://postgres:123456@localhost/FastAPI_Demo"

# Tạo động cơ kết nối (Engine)
engine = create_engine(URL_DATABASE)

# Tạo phiên làm việc (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo khuôn mẫu cơ sở cho các bảng (Base)
Base = declarative_base()

# --- PHẦN 2: ĐỊNH NGHĨA BẢNG (Model) ---


class MonAnDB(Base):
    __tablename__ = "mon_an"  # Tên bảng trong PostgreSQL

    id = Column(Integer, primary_key=True, index=True)
    ten_mon = Column(String, index=True)
    gia = Column(Float)
    mo_ta = Column(String, nullable=True)


# Lệnh này sẽ tự tạo bảng 'mon_an' trong DB nếu chưa có
Base.metadata.create_all(bind=engine)

# --- PHẦN 3: ĐỊNH NGHĨA DỮ LIỆU API (Pydantic) ---


class MonAnRequest(BaseModel):
    ten_mon: str
    gia: float
    mo_ta: str = None

# --- PHẦN 4: LOGIC PHỤ TRỢ (Dependency) ---
# Hàm này giúp mở kết nối DB khi có request và đóng lại khi xong


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- PHẦN 5: API ENDPOINTS ---
app = FastAPI()


@app.post("/them-mon")
def them_mon(mon: MonAnRequest, db: Session = Depends(get_db)):  # Dòng A
    # 1. Tạo object từ Model của SQLAlchemy
    mon_moi = MonAnDB(ten_mon=mon.ten_mon, gia=mon.gia,
                      mo_ta=mon.mo_ta)  # Dòng B

    # 2. Thêm vào phiên làm việc và Lưu (Commit)
    db.add(mon_moi)      # Dòng C
    db.commit()          # Dòng D
    db.refresh(mon_moi)  # Dòng E (Lấy lại ID vừa tự tạo)

    return mon_moi


@app.get("/danh-sach-mon")
def lay_danh_sach(db: Session = Depends(get_db)):
    danh_sach = db.query(MonAnDB).all()  # Dòng F
    return danh_sach
