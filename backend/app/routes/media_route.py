from fastapi import APIRouter, HTTPException
from app.schemas.pydantic.media import VideoGame, VideoGameCreate, Film, FilmCreate, Media
from app.dao.video_game_dao import VideoGameDAO
from app.dao.film_dao import FilmDAO
from app.dao.media_dao import MediaDAO
from app.auth.auth import *

media_router = APIRouter()

@media_router.get("/", tags=["media"], summary="Get all media", response_model=list[Media])
def get_all_media_contains_title(searchTitle: str , current_user: Annotated[User, Depends(get_current_user)]):
    try:
        media = MediaDAO().get_by_all_title_like(searchTitle)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all media")
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media

@media_router.post("/video-game", tags=["media"], summary="Create a new video-game", response_model=VideoGame)
def create_video_game(data: VideoGameCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        new_media_id = VideoGameDAO().create(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create video game")
    new_video_game = VideoGame(media_id=new_media_id, **data.model_dump())
    return new_video_game

@media_router.get("/video-game/{id}", tags=["media"], summary="Get video game by id", response_model=VideoGame)
def get_video_game_by_id(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        video_game = VideoGameDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get video game of id {id}")   
    if video_game is None:
        raise HTTPException(status_code=404, detail=f"Video game of id {id} not found")
    return video_game

@media_router.get("/video-game", tags=["media"], summary="Get all video games", response_model=list[VideoGame])
def get_all_video_games(current_user: Annotated[User, Depends(get_current_user)]):
    try:
        video_game_list = VideoGameDAO().get_all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all video games")
    return video_game_list

@media_router.put("/video-game/{id}", tags=["media"], summary="Update video game by id")
def update_video_game(id: int, data: VideoGameCreate, current_user: Annotated[User, Depends(get_current_user)]):
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
def delete_video_game(id: int, current_user: Annotated[User, Depends(get_current_user)]):
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


@media_router.post("/film", tags=["media"], summary="Create a new film", response_model=Film)
def create_film(data: FilmCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        new_media_id = FilmDAO().create(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create film")
    new_film = Film(media_id=new_media_id, **data.model_dump())
    return new_film

@media_router.get("/film/{id}", tags=["media"], summary="Get film by id", response_model=Film)
def get_film_by_id(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        film = FilmDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get film of id {id}")   
    if film is None:
        raise HTTPException(status_code=404, detail=f"Film of id {id} not found")
    return film

@media_router.get("/film", tags=["media"], summary="Get all films", response_model=list[Film])
def get_all_films(current_user: Annotated[User, Depends(get_current_user)]):
    try:
        film_list = FilmDAO().get_all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all films")
    return film_list

@media_router.put("/film/{id}", tags=["media"], summary="Update film by id")
def update_film(id: int, data: FilmCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        film = FilmDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get film of id {id}")
    if film is None:
        raise HTTPException(status_code=404, detail=f"Film of id {id} not found")
    film.title = data.title
    film.genre = data.genre
    film.rent_price = data.rent_price
    film.image_url = data.image_url
    film.media_description = data.media_description
    film.release_date = data.release_date
    film.rating = data.rating
    try:
        FilmDAO().update(film)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update film")

@media_router.delete("/film/{id}", tags=["media"], summary="Delete film by id")
def delete_film(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        film = FilmDAO().get_by_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get film of id {id}")
    if film is None:
        raise HTTPException(status_code=404, detail=f"Film of id {id} not found")
    try:
        FilmDAO().delete(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete film")