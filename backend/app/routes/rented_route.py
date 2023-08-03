from fastapi import APIRouter, HTTPException
from app.dao.rented_dao import RentedDao
from app.schemas.pydantic.rented import CreateRented, UpdateRented, Rented
from typing import List
from app.auth.auth import *

rented_router = APIRouter()

#create new rented instance
@rented_router.post("/rented/", tags=["rented"], summary="Create a new rented")
def create_rented(rented: CreateRented, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        RentedDao().create_rented(rented)
        raise HTTPException(status_code=200, detail="Rented created successfully")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create rented")

#delete rented instance
@rented_router.delete("/rented/{transaction_id}", tags=["rented"], summary="Delete a rented")
def delete_rented(transaction_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        RentedDao().delete_rented(transaction_id)
        raise HTTPException(status_code=200, detail="Rented deleted successfully")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete rented")

#get all rented items
@rented_router.get("/rented/", tags=["rented"], summary="Get all rented", response_model=List[Rented])
def get_all_rented(current_user: Annotated[User, Depends(get_current_user)]) -> List[Rented]:
    try:
        return RentedDao().get_all_rented()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all rented")

#get rented item by transaction id
@rented_router.get("/rented/{transaction_id}", tags=["rented"], summary="Get a rented by transaction id", response_model=Rented)
def get_rented_by_transaction_id(transaction_id: int, current_user: Annotated[User, Depends(get_current_user)]) -> Rented:
    try:
        return RentedDao().get_rented_by_transaction_id(transaction_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get rented by transaction id")

#update rented item
@rented_router.put("/rented/", tags=["rented"], summary="Update a rented")
def update_rented(rented: UpdateRented, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        RentedDao().update_rented(rented)
        return {"message": "Rented updated successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update rented")

#test rented object
{
    "transaction_id": 1,
    "media_id": 1
}
