from fastapi import APIRouter

from app.api.v1.endpoints import items, users, locations, login, shift

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(locations.router, prefix="/locations", tags=["locations"])
api_router.include_router(shift.router, prefix="/shifts", tags=["shifts"])
