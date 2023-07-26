from schemas.pydantic.media import VideoGame
from .media_dao import MediaDAO

class VideoGameDAO(MediaDAO):
    def create(self, video_game: VideoGame) -> int:
        media_id = super().create(video_game)  # Call the parent MediaDAO's create method
    
    def get_by_id(self, media_id: int) -> VideoGame | None:
        media = super().get_by_id(media_id)  # Call the parent MediaDAO's get_by_id method