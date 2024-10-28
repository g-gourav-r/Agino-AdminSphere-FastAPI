from fastapi import FastAPI
from views import admin_view, user_view
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],  # This allows all HTTP methods
    allow_headers=["*"],  # This allows all headers
)

app.include_router(admin_view.router)
app.include_router(user_view.router)

@app.get("/")
async def Ping():
    return {"ping success" : "Welcome to Agino AdminSphere API"}
