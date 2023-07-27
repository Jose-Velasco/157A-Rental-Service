from datetime import date
from app.schemas.pydantic.media import Media, MediaCreate
from pymysql import Connection
from app.models.database_manager import DatabaseManager

class MediaDAO:
    def __init__(self):
        self.connection = DatabaseManager.get_connection()

    def create(self, media: MediaCreate) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO Media (title, genre, rent_price, image_url, media_description, release_date, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (media.title, media.genre, media.rent_price, media.image_url, media.media_description, media.release_date, media.rating))
                self.connection.commit()
                return cursor.last_row_id
        except Exception as e:
            print(e)
            raise Exception("Error on create media")

    def get_by_id(self, id: int) -> Media | None:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Media WHERE id = %s"
                cursor.execute(sql, (id))
                result = cursor.fetchone()
                if result:
                    return Media(**result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"Error on get media of id {id}")

    def get_all(self) -> list[Media]:
        pass

    def update(self, media: Media) -> None:
        pass
    
    def delete(self, id: int) -> None:
        pass