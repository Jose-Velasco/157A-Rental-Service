from fastapi import APIRouter, HTTPException
from app.dao.cart_dao import CartDAO, InCartDAO
from app.schemas.pydantic.cart import InCart, CartCreate, Cart, CartBase
from app.schemas.pydantic.media import Film, VideoGame, MediaMixedOut

cart_router = APIRouter()

@cart_router.post("/", tags=["cart"], summary="Add a media to cart", response_model=Cart)
def create_cart(cart: CartCreate) -> Cart:
    """Create a new cart in database and return its id"""
    try:
        new_cart_id = CartDAO().create(cart)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create cart")
    return Cart(cart_id=new_cart_id, **cart.model_dump())

@cart_router.get("/{id}", tags=["cart"], summary="Get cart by id", response_model=Cart)
def get_cart_by_id(id: int) -> Cart:
    """Get a cart from database by its id"""
    try:
        cart = CartDAO().get_by_cart_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get cart of id {id}")   
    if cart is None:
        raise HTTPException(status_code=404, detail=f"Cart of id {id} not found")
    return cart

@cart_router.get("/user/{id}", tags=["cart"], summary="Get cart by user id", response_model=Cart)
def get_cart_by_user_id(id: int) -> Cart:
    """Get a cart from database by its user id"""
    try:
        cart = CartDAO().get_by_user_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get cart of user id {id}")   
    if cart is None:
        raise HTTPException(status_code=404, detail=f"Cart of user id {id} not found")
    return cart

@cart_router.get("/", tags=["cart"], summary="Get all carts", response_model=list[Cart])
def get_all_carts() -> list[Cart]:
    """Get all carts from database"""
    try:
        cart_list = CartDAO().get_all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all carts")
    return cart_list

@cart_router.delete("/{id}", tags=["cart"], summary="Delete cart by id")
def delete_cart(id: int):
    """Delete a cart from database by its id"""
    try:
        cart = CartDAO().get_by_cart_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get cart of id {id}")
    if cart is None:
        raise HTTPException(status_code=404, detail=f"Cart of id {id} not found")
    try:
        CartDAO().delete(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete cart")

@cart_router.post("/in", tags=["cart"], summary="Add a media to cart")
def create_in_cart(in_cart: InCart):
    """Add a media to cart"""
    in_cart_dao = InCartDAO()
    try:
        in_cart_record = in_cart_dao.get_record(in_cart)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get in cart record to create")
    if in_cart_record is not None:
        raise HTTPException(status_code=409, detail=f"Media of id {in_cart.media_id} already in cart of id {in_cart.cart_id}")
    try:
        in_cart_dao.create(in_cart)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create in cart")

@cart_router.get("/in/{cart_id}", tags=["cart"], summary="Get all In_Cart media and details by cart_id", response_model=MediaMixedOut)
def get_in_cart_media_details_by_cart_id(cart_id: int) -> MediaMixedOut:
    """Get all In_Cart record by cart_id"""
    try:
        films = InCartDAO().get_films_in_cart(cart_id)
        video_games = InCartDAO().get_video_games_in_cart(cart_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get all media details in cart of cart id {cart_id}")
    return MediaMixedOut(films=films, video_games=video_games)

@cart_router.get("/in/media/{media_id}", tags=["cart"], summary="Get cart_id that holds media of media_id", response_model=list[CartBase])
def get_cart_id_by_media_id(media_id: int) -> list[CartBase]:
    """Get cart_id that holds media of media_id"""
    try:
        cart_ids = InCartDAO().get_carts_id_by_media_id(media_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get cart of media id {media_id}")
    return cart_ids

@cart_router.delete("/in/remove", tags=["cart"], summary="Delete In_Cart record by media_id and cart_id")
def delete_in_cart_by_id(data: InCart):
    """Delete In_Cart record by media_id and cart_id (equivalent to removing media from cart)"""
    try:
        in_cart_media = InCartDAO().get_record(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get in_cart record to delete")
    if in_cart_media is None:
        raise HTTPException(status_code=404, detail=f"Media of id {data.media_id} not found in cart of id {data.cart_id}")
    try:
        InCartDAO().delete_record(data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete in cart")

@cart_router.delete("/in/remove/all/{cart_id}", tags=["cart"], summary="Delete all media in cart by cart_id")
def delete_all_in_cart_by_cart_id(cart_id: int):
    """Delete all media in cart by cart_id"""
    try:
        InCartDAO().delete_all_by_cart_id(cart_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on delete in cart of cart id {cart_id}")

@cart_router.get("/in/{id}/film", tags=["cart"], summary="Get all media in In_Cart of cart_id that are Films", response_model=list[Film])
def get_all_films_in_cart_by_cart_id(id: int) -> list[Film]:
    """Get all media in In_Cart of cart_id that are Films"""
    try:
        film_list = InCartDAO().get_films_in_cart(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get films in cart of cart id {id}")
    return film_list

@cart_router.get("/in/{id}/video-game", tags=["cart"], summary="Get all media in In_Cart of cart_id that are Video Games", response_model=list[VideoGame])
def get_all_video_games_in_cart_by_cart_id(id: int) -> list[VideoGame]:
    """Get all media in In_Cart of cart_id that are Video Games"""
    try:
        video_game_list = InCartDAO().get_video_games_in_cart(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error on get video games in cart of cart id {id}")
    return video_game_list

