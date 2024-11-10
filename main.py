from fastapi import FastAPI
from routes import auth, customer

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(customer.router, prefix="/customer", tags=["Customers"])

@app.get("/", tags=["Health Check"])
async def check_health_status():
    return {"status": "success", "message": "The API endpoint is working fine"}