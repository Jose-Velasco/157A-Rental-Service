from fastapi import APIRouter, HTTPException
from app.schemas.pydantic.media import VideoGame, VideoGameCreate
from app.dao.video_game_dao import VideoGameDAO

media_router = APIRouter()

@media_router.post("/video-game", tags=["media"], summary="Create a new video-game", response_model=VideoGame)
def create_video_game(data: VideoGameCreate):
    try:
        new_media_id = VideoGameDAO().create(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create video game")
    new_video_game = VideoGame(media_id=new_media_id, **data.model_dump())
    return new_video_game

@media_router.get("/video-game/{id}", tags=["media"], summary="Get video game by id", response_model=VideoGame)
def get_video_game_by_id(id: int):
    try:
        video_game = VideoGameDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get video game of id {id}")   
    if video_game is None:
        raise HTTPException(status_code=404, detail=f"Video game of id {id} not found")
    return video_game

@media_router.get("/video-game", tags=["media"], summary="Get all video games", response_model=list[VideoGame])
def get_all_video_games():
    try:
        video_game_list = VideoGameDAO().get_all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all video games")
    return video_game_list

@media_router.put("/video-game/{id}", tags=["media"], summary="Update video game by id")
def update_video_game(id: int, data: VideoGameCreate):
    try:
        video_game = VideoGameDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get video game of id {id}")
    if video_game is None:
        raise HTTPException(status_code=404, detail=f"Video game of id {id} not found")
    video_game.title = data.title
    video_game.genre = data.genre
    video_game.rent_price = data.rent_price
    video_game.image_url = data.image_url
    video_game.media_description = data.media_description
    video_game.release_date = data.release_date
    video_game.rating = data.rating
    try:
        VideoGameDAO().update(video_game)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update video game")

@media_router.delete("/video-game/{id}", tags=["media"], summary="Delete video game by id")
def delete_video_game(id: int):
    try:
        video_game = VideoGameDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get video game of id {id}")
    if video_game is None:
        raise HTTPException(status_code=404, detail=f"Video game of id {id} not found")
    try:
        VideoGameDAO().delete(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete video game")
