from app.schemas.pydantic.media import Film, FilmCreate
from app.dao.media_dao import MediaDAO

class FilmDAO(MediaDAO):
    def create(self, film: FilmCreate) -> int:
        media_id = super().create(film)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO Film (media_id, runtime, director) VALUES (%s, %s, %s)", (media_id, film.runtime, film.director))
                self.connection.commit()
                return media_id
        except Exception as e:
            print(e)
            raise Exception("Error on create film")
    
    def get_by_id(self, media_id: int) -> Film | None:
        media = super().get_by_id(media_id)
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT runtime, director FROM Film WHERE media_id = %s"
                cursor.execute(sql, (media_id))
                result = cursor.fetchone()
                if result:
                    return Film(**media.model_dump(), **result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"Error on get film of id {media_id}")
        
    def get_all(self) -> list[Film]:
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT M.media_id, M.title, M.genre, M.rent_price, M.image_url, M.media_description, M.release_date, M.rating, F.runtime, F.director
                    FROM Media M , Film F
                    WHERE M.media_id = F.media_id"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Film(**film) for film in result]
        except Exception as e:
            print(e)
            raise Exception("Error on get all films")
    
    def update(self, film: Film) -> None:
        super().update(film)
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE Film SET runtime = %s, director = %s WHERE media_id = %s"
                cursor.execute(sql, (film.runtime, film.director, film.media_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on update film")
    
    def delete(self, id: int) -> None:
        super().delete(id)
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM Film WHERE media_id = %s"
                cursor.execute(sql, (id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception("Error on delete film")
    