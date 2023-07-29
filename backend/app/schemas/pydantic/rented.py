from pydantic import BaseModel

# Shared properties
class RentedBase(BaseModel):
    transaction_id: int
    media_id: int

# Properties of a rented stored in DB (same as base)
class CreateRented(RentedBase):
    pass

class Rented(CreateRented):
    pass

class UpdateRented(RentedBase):
    pass
