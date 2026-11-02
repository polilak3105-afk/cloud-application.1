# Проектирование базы данных Cloud Application

## 1. Назначение базы данных
База данных предназначена для постоянного хранения информации об облачных сервисах приложения.

## 2. Сущности
### ServiceType
- `id` (INTEGER, PK) — уникальный идентификатор типа.
- `name` (VARCHAR(50)) — название типа (`application`, `database`, `monitoring`).
- `description` (VARCHAR(255)) — описание назначения типа.

### Service
- `id` (INTEGER, PK) — уникальный идентификатор сервиса.
- `name` (VARCHAR(100)) — название облачного сервиса.
- `type_id` (INTEGER, FK) — идентификатор типа сервиса.
- `status` (VARCHAR(20)) — текущее состояние сервиса (`running`, `maintenance`, `stopped`).

## 3. Связи
Связь между `ServiceType` и `Service` — **Один ко многим (1:N)**. Поле `services.type_id` является внешним ключом (`FK`), ссылающимся на `service_types.id`.

## 4. Логическая модель
```text
SERVICE_TYPES: id (PK), name, description
SERVICES: id (PK), name, type_id (FK), status

### Шаг 2. Выполните команды в терминале
Когда файл создан и сохранен в папке `docs/database_design.md`, выполните в терминале:

```powershell
git add docs/database_design.md
git commit -m "Add database design for Cloud Application"
git push origin docs/database-design