from fastapi import APIRouter, HTTPException
from app.dao.inventory_dao import InventoryDAO
from app.schemas.pydantic.inventory import InventoryCreate
from app.schemas.pydantic.inventory import InventoryUpdate
from typing import List
from app.auth.auth import *

inventory_router = APIRouter()

#create new inventory instance
@inventory_router.post("/inventory/", tags=["inventory"], summary="Create a new inventory")
def create_inventory(inventory: InventoryCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        InventoryDAO().create_inventory(inventory)
        return {"message": "Inventory created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create inventory")

#delete inventory instance
@inventory_router.delete("/inventory/{media_id}", tags=["inventory"], summary="Delete a inventory")
def delete_inventory(media_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        InventoryDAO().delete_inventory(media_id)
        return {"message": "Inventory deleted successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete inventory")
    

#get all available inventory items
@inventory_router.get("/inventory/available", tags=["inventory"], summary="Get all available inventory", response_model=List[InventoryUpdate])
def get_available_inventory(current_user: Annotated[User, Depends(get_current_user)]) -> List[InventoryUpdate]:
    try:
        return InventoryDAO().get_available_inventory()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get available inventory")

#check availability of a specific item
@inventory_router.get("/inventory/availability/{media_id}", tags=["inventory"], summary="Check availability of a specific item")
def check_availability(media_id: int, current_user: Annotated[User, Depends(get_current_user)]) -> bool:
    try:
        return InventoryDAO().check_availability(media_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on check availability")

#get all inventory items
@inventory_router.get("/inventory/", tags=["inventory"], summary="Get all inventory", response_model=List[InventoryUpdate])
def get_all_inventory(current_user: Annotated[User, Depends(get_current_user)]) -> List[InventoryUpdate]:
    try:
        return InventoryDAO().get_all_inventory()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all inventory")

#update inventory item
@inventory_router.put("/inventory/", tags=["inventory"], summary="Update a inventory")
def update_inventory(inventory: InventoryUpdate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        InventoryDAO().update_inventory(inventory)
        return {"message": "Inventory updated successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update inventory")








#test inventory object
{
    "media_id": 1,
    "rent_availability_status": True
}