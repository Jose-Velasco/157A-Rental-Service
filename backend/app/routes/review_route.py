from fastapi import APIRouter, HTTPException
from app.dao.review_dao import ReviewDAO
from app.dao.customer_dao import CustomerDAO
from app.schemas.pydantic.review import Review, ReviewCreate, ReviewSearchID, ReviewSearchMedia, ReviewUserInfo
from app.auth.auth import *


review_router = APIRouter()

@review_router.post("/create_review", tags=["review"], summary="Create a new review")
def create_review(review:ReviewCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        ReviewDAO().create_review(review)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create review")

@review_router.get("/search_review_by_id/{user_id}", tags=["review"], summary="Get a review by id")
def search_review_by_id(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return ReviewDAO().search_review_by_id(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get review by id")

@review_router.get("/search_review_by_media/{media_id}", tags=["review"], summary="Get a review by media id", response_model=list[ReviewSearchMedia])
def search_review_by_media(media_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return ReviewDAO().search_review_by_media(media_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get review by media")

@review_router.get("/search_review_by_media_id/{media_id}", tags=["review"], summary="Get a review by user id", response_model=list[ReviewUserInfo])
def get_reviews_by_media_id(media_id):
    try:
        reviews_w_User_info_output: list[ReviewUserInfo] = []
        review_dao = ReviewDAO()
        reviews: list[Review] = review_dao.get_reviews_details_by_media(media_id)
        for review in reviews:
            review_user_relation: ReviewSearchID = review_dao.get_review_relationship_record_by_id(review.review_id)
            user = CustomerDAO().get_customer_by_id(review_user_relation.user_id)
            reviews_w_User_info_output.append(ReviewUserInfo(**review.model_dump(), first_name=user.first_name, last_name=user.last_name, profile_pic_URL=user.profile_pic_URL))
        return reviews_w_User_info_output
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get review by media")
    

@review_router.put("/update_review/{review_id}", tags=["review"], summary="Update a review")
def update_review(review_id: int, review: ReviewCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        ReviewDAO().edit_review(review_id, review)
        raise HTTPException(status_code=200, detail="Review updated successfully")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update review")

@review_router.delete("/delete_review/{review_id}", tags=["review"], summary="Delete a review")
def delete_review(review_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        ReviewDAO().delete_review(review_id)
        raise HTTPException(status_code=200, detail="Review deleted successfully")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete review")

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


