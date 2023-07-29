from fastapi import APIRouter
from app.dao.review_dao import ReviewDAO
from app.dao.customer_dao import CustomerDAO
from app.schemas.pydantic.review import ReviewCreate 



review_router = APIRouter()

@review_router.post("/create_review")
def create_review(review:ReviewCreate):
    ReviewDAO().create_review(review)
    return{"message": "Review created successfully"}

@review_router.get("/search_review_by_id/{user_id}")
def search_review_by_id(user_id: int):
    reviews = ReviewDAO().search_review_by_id(user_id)
    return reviews

@review_router.get("/search_review_by_media/{media_id}")
def search_review_by_media(media_id: int):
    reviews = ReviewDAO().search_review_by_media(media_id)
    return reviews

@review_router.put("/update_review/{review_id}")
def update_review(review_id: int, review: ReviewCreate):
    ReviewDAO().edit_review(review_id, review)
    return {"message": "Review updated successfully"}

@review_router.delete("/delete_review/{review_id}")
def delete_review(review_id: int):
    ReviewDAO().delete_review(review_id)
    return {"message": "Review deleted successfully"}

{
    "media_id": 1,
    "user_id": 1,
    "publish_date": "2021-03-21",
    "content": "This is a review",
    "stars": 4
}

{
    "media_id": 1,
    "user_id": 1,
    "publish_date": "2021-04-21",
    "content": "This is a edited review",
    "stars": 2
}

{
    "user_id": 1,
}

{
    "media_id": 1,
}


