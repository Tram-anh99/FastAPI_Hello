from fastapi import FastAPI  # Dòng 1

app = FastAPI()              # Dòng 2


@app.get("/")                # Dòng 3
def xin_chao():              # Dòng 4
    return {"message": "Hello World"}  # Dòng 5
# ... (code cũ ở trên giữ nguyên)


@app.get("/chao/{ten}")      # Dòng 6
def chao_rieng(ma_id: str):    # Dòng 7
    return {"loi_chao": f"Xin chào bạn {ten}"}  # Dòng 8
