from pydantic import BaseModel
from datetime import date


#Shared properties 
class ReviewBase(BaseModel):
    review_id: int
    user_id: int
    media_id: int
    publish_date: date 
    content: str
    stars: int

#Properties of a review stored in DB (same as base)
class Review(ReviewBase):
    pass

#Properties needed in order to make a new review (same as base)
class ReviewCreate(ReviewBase):
    pass

#Properties needed in order to edit an existing review (same as base)
class ReviewEdit(ReviewBase):
    pass

