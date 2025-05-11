from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "🟢 Working"}

@app.get("/home")
async def home():
    return {"message": "Hello World"}

@app.get("/env")
async def env_settings():
    return {
        "app_name": os.getenv("APP_NAME", "FastAPI App"),
        "version": os.getenv("APP_VERSION", "1.0"),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "api_base_url": os.getenv("API_BASE_URL", "http://localhost"),
        "timeout_seconds": os.getenv("TIMEOUT_SECONDS", "30"),
        "region": os.getenv("REGION", "us-east-1")
    }   