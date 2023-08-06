from fastapi import APIRouter, HTTPException
from app.dao.returned_dao import ReturnedDAO
from app.auth.auth import *
from app.schemas.pydantic.returned import Return

returned_router = APIRouter()

#set returned
@returned_router.post("/returned/", tags=["returned"], summary="Set returned")
def set_returned(returned: Return, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        ReturnedDAO().set_returned(returned)
        return {"message": "Returned set successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on set returned")

#get all returned
@returned_router.get("/returned/{user_id}", tags=["returned"], summary="Get all returned", response_model=dict)
def get_all_returned(user_id: int, current_user: Annotated[User, Depends(get_current_user)]) -> dict:
    try:
        return ReturnedDAO().get_all_returned(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all returned")
