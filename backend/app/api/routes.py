
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.deps import get_db


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "NexusOne AI API is running"
    }


@router.get("/database-health")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "connected",
            "message": "PostgreSQL database is working"
        }

    except Exception as error:
        return {
            "status": "disconnected",
            "message": str(error)
        }
