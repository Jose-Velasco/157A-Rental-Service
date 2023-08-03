from fastapi import APIRouter
from app.auth.auth import *
from typing import Annotated
from app.dao.employee_dao import EmployeeDAO
from app.schemas.pydantic.user import User, Employee
from app.dao.customer_dao import CustomerDAO


auth_router = APIRouter()

@auth_router.get("/test/")
def read_root():
    return {"HelloWorld!!": "Hello"} 

@auth_router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/users/me/")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    #If they're an employee
    found_employee = EmployeeDAO().get_employee_by_id(current_user.user_id)
    return found_employee if found_employee is not None else current_user
    






