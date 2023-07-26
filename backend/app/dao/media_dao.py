from schemas.pydantic.media import Media
from pymysql import Connection

class MediaDAO:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, name: str, url: str) -> int:
        pass

    def get_by_id(self, id: int) -> Media | None:
        pass

    def get_all(self) -> list[Media]:
        pass

    def update(self, media: Media) -> None:
        pass
    
    def delete(self, id: int) -> None:
        pass