from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "🟢 Working"}

@app.get("/home")
async def home():
    return {"message": "Hello World"}