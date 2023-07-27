from app.schemas.pydantic.media import Media, MediaCreate
from app.models.database_manager import DatabaseManager

class MediaDAO:
    def __init__(self):
        self.connection = DatabaseManager().get_connection()

    def create(self, media: MediaCreate) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO Media (title, genre, rent_price, image_url, media_description, release_date, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (media.title, media.genre, media.rent_price, media.image_url, media.media_description, media.release_date, media.rating))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            print(e)
            raise Exception("Error on create media")

    def get_by_id(self, id: int) -> Media | None:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Media WHERE media_id = %s"
                cursor.execute(sql, (id))
                result = cursor.fetchone()
                if result:
                    return Media(**result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"Error on get media of id {id}")

    def get_all(self) -> list[Media]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Media"
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Media(**media) for media in result]
        except Exception as e:
            print(e)
            raise Exception("Error on get all media")

    def update(self, media: Media) -> None:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE Media SET title = %s, genre = %s, rent_price = %s, image_url = %s, media_description = %s, release_date = %s, rating = %s WHERE media_id = %s"
                cursor.execute(sql, (media.title, media.genre, media.rent_price, media.image_url, media.media_description, media.release_date, media.rating, media.media_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on update media")
    
    def delete(self, id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM Media WHERE media_id = %s"
                cursor.execute(sql, (id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"Error on delete media of id {id}")