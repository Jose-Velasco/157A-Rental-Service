from pydantic import BaseModel

# Shared properties
class AddressBase(BaseModel):
    user_id: int
    street: str
    city: str
    state: str
    zip_code: int
    country: str

# Properties of an address stored in DB (same as base)
class Address(AddressBase):
    pass

# Properties needed in order to make a new address (same as base)
class AddressCreate(AddressBase):
    pass

# Properties needed in order to update an address (same as base)
class AddressUpdate(AddressBase):
    pass

