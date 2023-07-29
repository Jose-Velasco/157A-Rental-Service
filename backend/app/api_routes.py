from fastapi import APIRouter
from app.routes.authentication import auth_router

from app.routes.user_route import user_router
from app.routes.review_route import review_router

# registration of all system routes
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])

api_router.include_router(user_router, prefix="/user", tags=["user"])

api_router.include_router(review_router, prefix="/review", tags=["review"])
