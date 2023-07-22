from fastapi import APIRouter
from app.routes.authentication import auth_router

# registration of all system routes
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])