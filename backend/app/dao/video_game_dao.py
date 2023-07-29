from app.schemas.pydantic.media import VideoGame
from app.dao.media_dao import MediaDAO

class VideoGameDAO(MediaDAO):
    def create(self, video_game: VideoGame) -> int:
        media_id = super().create(video_game)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO Video_Game (media_id, publisher, developer) VALUES (%s, %s, %s)", (media_id, video_game.publisher, video_game.developer))
                self.connection.commit()
                return media_id
        except Exception as e:
            print(e)
            raise Exception("Error on create video game")

    
    def get_by_id(self, media_id: int) -> VideoGame | None:
        media = super().get_by_id(media_id)
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT publisher, developer FROM Video_Game WHERE media_id = %s"
                cursor.execute(sql, (media_id))
                result = cursor.fetchone()
                if result:
                    return VideoGame(**media.model_dump(), **result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"Error on get video game of id {media_id}")
    
    def get_all(self) -> list[VideoGame]:
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT M.media_id, M.title, M.genre, M.rent_price, M.image_url, M.media_description, M.release_date, M.rating, V.publisher, V.developer
                    FROM Media M , Video_Game V
                    WHERE M.media_id = V.media_id"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return [VideoGame(**video_game) for video_game in result]
        except Exception as e:
            print(e)
            raise Exception("Error on get all video games")
        
    def update(self, video_game: VideoGame) -> None:
        super().update(video_game)
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE Video_Game SET publisher = %s, developer = %s WHERE media_id = %s"
                cursor.execute(sql, (video_game.publisher, video_game.developer, video_game.media_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on update video game")
        
    def delete(self, media_id: int) -> None:
        super().delete(media_id)
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM Video_Game WHERE media_id = %s"
                cursor.execute(sql, (media_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"Error on delete video game of id {media_id}")