from fastapi import APIRouter
from app.routers.services import count_services

# Создаем роутер с тегом System
router = APIRouter(
    tags=["System"]
)


@router.get("/status")
def status():
    return {
        "status": "ok",
        "service": "Cloud Application"
    }


@router.get("/about")
def about():
    return {
        "name": "Cloud Application",
        "type": "server application",
        "language": "Python",
        "framework": "FastAPI"
    }


@router.get("/service-count")
def service_count_endpoint():
    return {
        "services": count_services()
    }

