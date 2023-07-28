from pydantic import BaseModel

# Shared properties
class InventoryBase(BaseModel):
    media_id: int
    rent_availability_status: bool

# Properties of an inventory stored in DB (same as base)
class Inventory(InventoryBase):
    pass

# Properties needed in order to make a new inventory (same as base)
class InventoryCreate(InventoryBase):
    pass

# Properties needed in order to update an inventory (same as base)
class InventoryUpdate(InventoryBase):
    pass
