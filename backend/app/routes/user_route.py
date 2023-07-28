from fastapi import APIRouter
from app.dao.customer_dao import CustomerDAO
from app.dao.employee_dao import EmployeeDAO
from app.schemas.pydantic.user import CustomerCreate


user_router = APIRouter()

@user_router.post("/customer/")
def create_user(customer: CustomerCreate):
    CustomerDAO().create_customer(customer)
    return {"message": "Customer created successfully"}


#create test customer object for me on multiple lines
{
    "password": "password",
    "first_name": "John",
    "last_name": "Doe",
    "birthday": "1990-01-01",
    "profile_pic_URL": "https://www.google.com",
    "age": 30,
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
            "email": "john.doe@gmail"
        }
    ]
}


