from schemas.pydantic.media import Film
from .media_dao import MediaDAO

class FilmDAO(MediaDAO):
    def create(self, film: Film) -> int:
        media_id = super().create(film)  # Call the parent MediaDAO's create method
    
    def get_by_id(self, media_id: int) -> Film | None:
        media = super().get_by_id(media_id)  # Call the parent MediaDAO's get_by_id method