from fastapi import APIRouter, HTTPException, Path
from app.models import ServiceCreate

# Создаем роутер с префиксом /services и тегом Services
router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

# Временное хранилище данных
services = [
    {
        "id": 1,
        "name": "Web Service",
        "type": "application",
        "status": "running"
    },
    {
        "id": 2,
        "name": "Database Service",
        "type": "database",
        "status": "running"
    }
]

# --- Сервисный слой (логика работы с данными) ---

def get_all_services():
    return services

def get_service_by_id(service_id: int):
    for service in services:
        if service["id"] == service_id:
            return service
    return None

def create_service(service: ServiceCreate):
    new_id = max(item["id"] for item in services) + 1 if services else 1
    new_service = {
        "id": new_id,
        "name": service.name,
        "type": service.type,
        "status": service.status
    }
    services.append(new_service)
    return new_service

def update_service(service_id: int, service: ServiceCreate):
    for item in services:
        if item["id"] == service_id:
            item["name"] = service.name
            item["type"] = service.type
            item["status"] = service.status
            return item
    return None

def delete_service(service_id: int):
    for item in services:
        if item["id"] == service_id:
            services.remove(item)
            return item
    return None


# --- Маршруты (Эндпоинты) API ---

@router.get(
    "",
    summary="Получить список сервисов"
)
def read_services():
    return get_all_services()


@router.get(
    "/{service_id}",
    summary="Получить сервис по идентификатору",
    description="Возвращает сервис с указанным идентификатором.",
    responses={
        404: {
            "description": "Сервис не найден"
        }
    }
)
def read_service(
    service_id: int = Path(
        ...,
        description="Уникальный идентификатор сервиса",
        gt=0
    )
):
    service = get_service_by_id(service_id)

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service


@router.post(
    "",
    summary="Создать новый сервис",
    description=(
        "Создаёт новый облачный сервис "
        "на основе переданных данных."
    ),
    status_code=201
)
def create_service_endpoint(
    service: ServiceCreate
):
    return create_service(service)


@router.put(
    "/{service_id}",
    summary="Изменить сервис",
    description="Изменяет данные существующего сервиса.",
    responses={
        404: {
            "description": "Сервис не найден"
        }
    }
)
def update_service_endpoint(
    service_id: int = Path(..., gt=0),
    service: ServiceCreate = None
):
    updated_service = update_service(
        service_id,
        service
    )

    if updated_service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return updated_service


@router.delete(
    "/{service_id}",
    summary="Удалить сервис",
    responses={
        404: {
            "description": "Сервис не найден"
        }
    }
)
def delete_service_endpoint(
    service_id: int = Path(..., gt=0)
):
    deleted_service = delete_service(service_id)

    if deleted_service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return {
        "message": "Service deleted",
        "id": service_id
    }

def count_services():
    return len(services)