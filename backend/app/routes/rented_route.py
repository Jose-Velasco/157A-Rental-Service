from fastapi import APIRouter
from app.dao.rented_dao import RentedDao
from app.schemas.pydantic.rented import CreateRented, UpdateRented, Rented
from typing import List

rented_router = APIRouter()

#create new rented instance
@rented_router.post("/rented/")
def create_rented(rented: CreateRented):
    RentedDao().create_rented(rented)
    return {"message": "Rented created successfully"}

#delete rented instance
@rented_router.delete("/rented/{transaction_id}")
def delete_rented(transaction_id: int):
    RentedDao().delete_rented(transaction_id)
    return {"message": "Rented deleted successfully"}

#get all rented items
@rented_router.get("/rented/")
def get_all_rented() -> List[Rented]:
    return RentedDao().get_all_rented()

#get rented item by transaction id
@rented_router.get("/rented/{transaction_id}")
def get_rented_by_transaction_id(transaction_id: int) -> Rented:
    return RentedDao().get_rented_by_transaction_id(transaction_id)

#update rented item
@rented_router.put("/rented/")
def update_rented(rented: UpdateRented):
    RentedDao().update_rented(rented)
    return {"message": "Rented updated successfully"}

#test rented object
{
    "transaction_id": 1,
    "media_id": 1
}
