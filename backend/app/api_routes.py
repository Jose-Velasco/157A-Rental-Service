from fastapi import APIRouter
from app.routes.authentication import auth_router
from app.routes.media import media_router

# registration of all system routes
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(media_router, prefix="/media", tags=["media"])