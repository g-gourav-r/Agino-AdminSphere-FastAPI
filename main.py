from fastapi import FastAPI
from views import admin_view

app = FastAPI()

# Include routers

app.include_router(admin_view.router)
