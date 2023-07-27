from pydantic import BaseModel

# Shared properties
class AddressBase(BaseModel):
    
    street: str
    city: str
    state: str
    zip_code: int
    country: str

# Properties of an address stored in DB (same as base)
class Address(AddressBase):
    user_id: int

# Properties needed in order to make a new address (same as base)
class AddressCreate(AddressBase):
    user_id: int

# Properties needed in order to update an address (same as base)
class AddressUpdate(AddressBase):
    pass

