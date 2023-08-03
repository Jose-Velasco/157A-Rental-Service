from pydantic import BaseModel

class CartBase(BaseModel):
    user_id: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    user_id: int
    cart_id: int

class InCart(BaseModel):
    media_id: int
    cart_id: int

class CartSubmit(Cart):
    rent_duration: int