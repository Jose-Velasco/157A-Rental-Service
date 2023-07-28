from fastapi import APIRouter
from app.dao.inventory_dao import InventoryDAO
from app.schemas.pydantic.inventory import InventoryCreate
from app.schemas.pydantic.inventory import InventoryUpdate
from typing import List

inventory_router = APIRouter()

@inventory_router.post("/inventory/")
def create_inventory(inventory: InventoryCreate):
    InventoryDAO().create_inventory(inventory)
    return {"message": "Inventory created successfully"}

@inventory_router.delete("/inventory/{media_id}")
def delete_inventory(media_id: int):
    InventoryDAO().delete_inventory(media_id)
    return {"message": "Inventory deleted successfully"}

@inventory_router.get("/inventory/available")
def get_available_inventory() -> List[InventoryUpdate]:
    return InventoryDAO().get_available_inventory()

@inventory_router.get("/inventory/availability/{media_id}")
def check_availability(media_id: int) -> bool:
    return InventoryDAO().check_availability(media_id)

@inventory_router.put("/inventory/")
def update_inventory(inventory: InventoryUpdate):
    InventoryDAO().update_inventory(inventory)
    return {"message": "Inventory updated successfully"}








#test inventory object
{
    "media_id": 1,
    "rent_availability_status": True
}