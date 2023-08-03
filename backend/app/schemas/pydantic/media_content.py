from pydantic import BaseModel
from datetime import date

class MediaContentBase(BaseModel):
    title: str
    genre: str
    image_url: str
    media_description: str
    release_date: date
    rating: str

class MediaContentCreate(MediaContentBase):
    pass

class MediaContent(MediaContentBase):
    pass

class UpdateMediaContent(MediaContentBase):
    pass