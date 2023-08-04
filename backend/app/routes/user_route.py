from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.dao.customer_dao import CustomerDAO, Customer
from app.dao.employee_dao import EmployeeDAO, Employee
from app.schemas.pydantic.user import CustomerCreate
from app.schemas.pydantic.user import EmployeeCreate
from app.auth.auth import *
from typing import List



user_router = APIRouter()

@user_router.post("/customer/", tags=["user"], summary="Create a new customer")
def create_user(customer: CustomerCreate):
    try:
        CustomerDAO().create_customer(customer)
        return {"message": "Customer created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create customer")
    

@user_router.post("/employee/", tags=["user"], summary="Create a new employee")
def create_employee(employee: EmployeeCreate):
    try:
        EmployeeDAO().create_employee(employee)
        return {"message": "Employee created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create employee")

@user_router.get("/customer/{user_id}", tags=["user"], summary="Get a customer by id", response_model=Customer)
def get_customer_by_id(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return CustomerDAO().get_customer_by_id(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get customer by id")

@user_router.get("/employee/{user_id}", tags=["user"], summary="Get an employee by id", response_model=Employee)
def get_employee_by_id(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return EmployeeDAO().get_employee_by_id(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get employee by id")
    


@user_router.get("/customer/", tags=["user"], summary="Get all customers", response_model=List[Customer])
async def get_all_customers(current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return CustomerDAO().get_all_customers()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all customers")
    

@user_router.get("/employee/", tags=["user"], summary="Get all employees", response_model=List[Employee])
def get_all_employees(current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return EmployeeDAO().get_all_employees()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all employees")
    

@user_router.put("/customer/{user_id}", tags=["user"], summary="Update a customer")
def update_customer(user_id: int, customer: CustomerCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        CustomerDAO().update_customer(user_id, customer)
        return {"message": "Customer updated successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update customer")

@user_router.put("/employee/{user_id}", tags=["user"], summary="Update an employee")
def update_employee(user_id: int, employee: EmployeeCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        EmployeeDAO().update_employee(user_id, employee)
        return {"message": "Employee updated successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update employee")

@user_router.delete("/customer/{user_id}", tags=["user"], summary="Delete a customer")
def delete_customer(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        CustomerDAO().delete_customer(user_id)
        return {"message": "Customer deleted successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete customer")
    

@user_router.delete("/employee/{user_id}", tags=["user"], summary="Delete an employee")
def delete_employee(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        EmployeeDAO().delete_employee(user_id)
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete employee")
    

#create test employee object for me on multiple lines
{
    "first_name": "John",
    "last_name": "Cena",
    "birthday": "1990-01-01",
    "profile_pic_URL": "https://www.google.com",
    "age": 30,
    "phone_number": "1234567890",
    "address": [
        {
            "street": "123 Main St",
            "city": "New York",
            "zip_code": "12345",
            "state": "NY",
            "country": "USA"
        }
    ],
    "email": [
        {
            "email": "john@yahoo.com"
        }
    ],
    "ssn": 8885555,
    "salary": 100000,
    "start_date": "2020-01-01",
    "employee_type": "Manager",
    "username": "cenajohn",
    "password": "cena123"
}




