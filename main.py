from fastapi import FastAPI
from routes import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/", tags=["Health Check"])
async def check_health_status():
    return {"status": "success", "message": "The API endpoint is working fine"}