from fastapi import APIRouter, HTTPException
from app.schemas.pydantic.media import VideoGame, VideoGameCreate, Film, FilmCreate, MediaUpdate
from app.schemas.pydantic.media_content import MediaContent, MediaContentWithMediaId
from app.dao.video_game_dao import VideoGameDAO
from app.dao.film_dao import FilmDAO
from app.dao.media_dao import MediaDAO
from app.auth.auth import *

media_router = APIRouter()

@media_router.get("/search", tags=["media"], summary="Get all media with title like searchTitle", response_model=list[MediaContentWithMediaId])
def get_all_media_contains_title(searchTitle: str , current_user: Annotated[User, Depends(get_current_user)]):
    try:
        media_content = MediaDAO().get_by_all_title_like(searchTitle)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all media")
    if media_content is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media_content

@media_router.get("/details/{media_id}", tags=["media"], summary="Get all media details by media_id", response_model=VideoGame | Film)
def get_all_media_details_by_id(media_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        detailed_results: VideoGame = VideoGameDAO().get_by_id(media_id)
        if detailed_results is None:
            detailed_results: Film = FilmDAO().get_by_id(media_id)
        if detailed_results is None:
            raise HTTPException(status_code=404, detail="Media not found")
        return detailed_results
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get media")


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
    video_game.image_url = data.image_url
    video_game.media_description = data.media_description
    video_game.release_date = data.release_date
    video_game.rating = data.rating
    video_game.publisher = data.publisher
    video_game.developer = data.developer
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
    film.image_url = data.image_url
    film.media_description = data.media_description
    film.release_date = data.release_date
    film.rating = data.rating
    film.runtime = data.runtime
    film.director = data.director
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
    
@media_router.put("/update_title", tags=["media"], summary="Update media's title")
def update_media_title(data: MediaUpdate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        MediaDAO().update_title(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update media title")

#create  real video game below in json
{
    "title": "The Legend of Zelda: Breath of the Wild",
    "genre": "Action-adventure",
    "image_url": "https://upload.wikimedia.org/wikipedia/en/1/19/The_Legend_of_Zelda_Breath_of_the_Wild.jpg",
    "media_description": "The Legend of Zelda: Breath of the Wild[a] is a 2017 action-adventure game developed and published by Nintendo for the Nintendo Switch and Wii U consoles. Breath of the Wild is part of the Legend of Zelda franchise and is set at the end of the series' timeline; the player controls Link, who awakens from a hundred-year slumber to defeat Calamity Ganon before it can destroy the kingdom of Hyrule.",
    "release_date": "2017-03-03",
    "rating": 10,
    "publisher": "Nintendo",
    "developer": "Nintendo Entertainment Planning & Development"
}

#create  real film below in json
{
    "title": "The Shawshank Redemption",
    "genre": "Drama",
    "image_url": "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
    "media_description": "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the 1982 Stephen King novella Rita Hayworth and Shawshank Redemption. It tells the story of banker Andy Dufresne (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murders of his wife and her lover, despite his claims of innocence. Over the following two decades, he befriends a fellow prisoner, contraband smuggler Ellis \"Red\" Redding (Morgan Freeman), and becomes instrumental in a money-laundering operation led by the prison warden Samuel Norton (Bob Gunton). William Sadler, Clancy Brown, Gil Bellows, and James Whitmore appear in supporting roles.",
    "release_date": "1994-09-23",
    "rating": "R",
    "runtime": 142,
    "director": "Frank Darabont"
}




