from fastapi import FastAPI  # Dòng 1

app = FastAPI()              # Dòng 2


# ... code cũ giữ nguyên

@app.get("/tim-kiem")               # Dòng 9: KHÔNG có {tu_khoa} ở đây
def tim_mon_an(tu_khoa: str, limit: int = 10):  # Dòng 10
    return {
        "ket_qua": f"Đang tìm món '{tu_khoa}'",
        "so_luong_hien_thi": limit
    }
