from datetime import date
from pydantic import BaseModel

# Shared properties
# before creating an item, we don't know what will be the ID assigned to it
class MediaBase(BaseModel):
    title: str
    genre: str
    rent_price: int
    image_url: str
    media_description: str
    release_date: date
    rating: str

# Properties shared by Media stored in DB
# when reading it (when returning it from the API) we will already know its ID
class Media(MediaBase):
    media_id: int

# Properties to receive on Media creation (currenly the same as base)
class MediaCreate(MediaBase):
    pass

# Properties to receive on Media update (currenly the same as base)
class MediaUpdate(MediaBase):
    pass

# Shared video game properties
class VideoGameBase(MediaBase):
    publisher: str
    developer: str

# Properties shared by Video Game stored in DB
class VideoGame(VideoGameBase):
    media_id: int

# Properties to receive on video game creation (currenly the same as base video game)
class VideoGameCreate(VideoGameBase):
    pass

# Properties to receive on video game update (currenly the same as base video game)
class VideoGameUpdate(VideoGameBase):
    pass

class FilmBase(MediaBase):
    runtime: int
    director: str

class Film(FilmBase):
    media_id: int

class FilmCreate(FilmBase):
    pass

class FilmUpdate(FilmBase):
    pass

class MediaMixedOut(BaseModel):
    films: list[Film]
    video_games: list[VideoGame]