from fastapi import FastAPI  # Dòng 1

app = FastAPI()              # Dòng 2

@app.get("/")                # Dòng 3
def xin_chao():              # Dòng 4
    return {"message": "Hello World"}  # Dòng 5