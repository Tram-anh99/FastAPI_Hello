from fastapi import FastAPI  # Dòng 1
from pydantic import BaseModel  # Dòng A: Import mới
app = FastAPI()              # Dòng 2


@app.get("/")                # Dòng 3
def xin_chao():              # Dòng 4
    return {"message": "Hello World"}  # Dòng 5
# ... (code cũ ở trên giữ nguyên)


@app.get("/chao/{ma_id}")      # Dòng 6
def chao_rieng(ma_id: int):    # Dòng 7
    return {"loi_chao": f"Xin chào bạn {ma_id}"}  # Dòng 8
# ... code cũ giữ nguyên


@app.get("/tim-kiem")               # Dòng 9: KHÔNG có {tu_khoa} ở đây
def tim_mon_an(tu_khoa: str, limit: int = 10):  # Dòng 10
    return {
        "ket_qua": f"Đang tìm món '{tu_khoa}'",
        "so_luong_hien_thi": limit
    }


class MonAn(BaseModel):         # Dòng B
    ten_mon: str
    gia: float
    mo_ta: str = None           # Dòng C


@app.post("/them-mon")          # Dòng D
def them_mon_moi(mon: MonAn):   # Dòng E
    return {
        "thong_bao": "Thêm món thành công",
        "ten": mon.ten_mon,
        "gia_ban": mon.gia,
            "mo_ta": mon.mo_ta
    }
