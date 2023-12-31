from fastapi import APIRouter
from app.routes.authentication import auth_router
from app.routes.transaction_route import transaction_router
from app.routes.user_route import user_router
from app.routes.returned_route import returned_router
from app.routes.review_route import review_router
from app.routes.media_route import media_router
from app.routes.inventory_route import inventory_router
from app.routes.rented_route import rented_router
from app.routes.cart_route import cart_router


# registration of all system routes
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])

api_router.include_router(user_router, prefix="/user", tags=["user"])

api_router.include_router(review_router, prefix="/review", tags=["review"])

api_router.include_router(media_router, prefix="/media", tags=["media"])

api_router.include_router(inventory_router, prefix="/inv", tags=["inventory"])

api_router.include_router(transaction_router, prefix="/tran", tags=["transaction"])

api_router.include_router(rented_router, prefix="/rent", tags=["rented"])

api_router.include_router(cart_router, prefix="/cart", tags=["cart"])   

api_router.include_router(returned_router, prefix="/ret", tags=["returned"])