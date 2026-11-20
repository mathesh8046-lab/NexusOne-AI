

from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.routes import router
from app.api.ai_requests import router as ai_requests_router

app = FastAPI(
    title="NexusOne AI",
    description="Adaptive Multi-Agent Decision Intelligence Platform",
    version="1.0.0"
)


app.include_router(router, prefix="/api/v1")
app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)
app.include_router(
    ai_requests_router,
    prefix="/api/v1/ai-requests",
    tags=["AI Requests"]
)

@app.get("/")
def home():
    return {
        "message": "Welcome to NexusOne AI!",
        "status": "Backend is running successfully"
    }
