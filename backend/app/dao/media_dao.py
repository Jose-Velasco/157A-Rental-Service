from app.schemas.pydantic.media import Media, MediaCreate, MediaUpdate
from app.schemas.pydantic.media_content import MediaContentCreate, MediaContent, UpdateMediaContent, MediaContentWithMediaId
from app.models.database_manager import DatabaseManager

class MediaDAO:
    def __init__(self):
        self.connection = DatabaseManager().get_connection()

    def create(self, media: MediaContentCreate) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO Media (title) VALUES (%s)"
                cursor.execute(sql, (media.title))
                self.connection.commit()
                media_id = cursor.lastrowid
                sql = "INSERT INTO Media_Content (title, genre, image_url, media_description, release_date, rating) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (media.title, media.genre, media.image_url, media.media_description, media.release_date, media.rating))
                self.connection.commit()
                return media_id
        except Exception as e:
            print(e)
            raise Exception("Error on create media")

    def get_by_id(self, id: int) -> MediaContent | None:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Media_Content MC, Media M WHERE MC.title = M.title AND M.media_id = %s"
                cursor.execute(sql, (id))
                result = cursor.fetchone()
                if result:
                    return MediaContent(title=result["title"], genre=result["genre"], image_url=result["image_url"], media_description=result["media_description"], release_date=result["release_date"], rating=result["rating"])
                return None
        except Exception as e:
            print(e)
            raise Exception(f"Error on get media of id {id}")
        
    def get_by_all_title_like(self, title: str) -> list[MediaContentWithMediaId] | None:
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT * 
                         FROM Media_Content MC, Media M
                         WHERE M.title LIKE %s AND MC.title = M.title"""
                cursor.execute(sql, (f"%{title}%"))
                result = cursor.fetchall()
                if result:
                    return [MediaContentWithMediaId(**media_content) for media_content in result]
                return None
        except Exception as e:
            print(e)
            raise Exception(f"DAO error: Error on get media of title {title}")

    def get_all(self) -> list[MediaContent]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Media_Content"
                cursor.execute(sql)
                result = cursor.fetchall()
                return [MediaContent(**media_content) for media_content in result]
        except Exception as e:
            print(e)
            raise Exception("Error on get all media")

    def update(self, media: UpdateMediaContent) -> None:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE Media_Content SET genre = %s, image_url = %s, media_description = %s, release_date = %s, rating = %s WHERE title = %s"
                cursor.execute(sql, (media.genre, media.image_url, media.media_description, media.release_date, media.rating, media.title))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on update media")
    
    def update_title(self, media_update: MediaUpdate) -> None:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE Media SET title = %s WHERE media_id = %s"
                cursor.execute(sql, (media_update.title, media_update.media_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on update media title")

    def delete(self, id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM Media WHERE media_id = %s"
                cursor.execute(sql, (id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"Error on delete media of id {id}")