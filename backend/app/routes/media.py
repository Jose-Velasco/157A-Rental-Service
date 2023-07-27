from fastapi import APIRouter
from app.schemas.pydantic.media import MediaCreate, Media
from app.dao.media_dao import MediaDAO
from app.configs.api_config import settings
import pymysql

media_router = APIRouter()

@media_router.post("/", tags=["media"], summary="Create a new media", response_model=MediaCreate)
def create_media(data: MediaCreate):
    try:
        connection = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        media = MediaDAO(connection).create(data.title, data.genre, data.rent_price, data.image_url, data.media_description, data.release_date, data.rating)
    except Exception as e:
        print(e)
        raise Exception("Error on create media")
    print(data)
    return data
    