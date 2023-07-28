from fastapi import APIRouter
from app.dao.review_dao import ReviewDAO
from app.dao.customer_dao import CustomerDAO
from app.schemas.pydantic.review import ReviewCreate 



review_router = APIRouter()

@review_router.post("/create_review")
def create_review(review:ReviewCreate):
    ReviewDAO().create_review(review)
    return{"message": "Review created successfully"}

{
    "media_id": 1,
    "user_id": 1,
    "publish_date": "2021-03-21",
    "content": "This is a review",
    "stars": 4
}

