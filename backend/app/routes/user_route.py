from fastapi import APIRouter
from app.dao.customer_dao import CustomerDAO
from app.dao.employee_dao import EmployeeDAO
from app.schemas.pydantic.user import CustomerCreate
from app.schemas.pydantic.user import EmployeeCreate


user_router = APIRouter()

@user_router.post("/customer/")
def create_user(customer: CustomerCreate):
    CustomerDAO().create_customer(customer)
    return {"message": "Customer created successfully"}

@user_router.post("/employee/")
def create_employee(employee: EmployeeCreate):
    EmployeeDAO().create_employee(employee)
    return {"message": "Employee created successfully"}

@user_router.get("/customer/{user_id}")
def get_customer_by_id(user_id: int):
    customer = CustomerDAO().get_customer_by_id(user_id)
    return {"Customer": customer}

@user_router.get("/employee/{user_id}")
def get_employee_by_id(user_id: int):
    employee = EmployeeDAO().get_employee_by_id(user_id)
    return {"Employee": employee}

@user_router.get("/customer/")
def get_all_customers():
    customers = CustomerDAO().get_all_customers()
    return {"Customers": customers}

@user_router.get("/employee/")
def get_all_employees():
    employees = EmployeeDAO().get_all_employees()
    return {"Employees": employees}

@user_router.put("/customer/{user_id}")
def update_customer(user_id: int, customer: CustomerCreate):
    CustomerDAO().update_customer(user_id, customer)
    return {"message": "Customer updated successfully"}

@user_router.put("/employee/{user_id}")
def update_employee(user_id: int, employee: EmployeeCreate):
    EmployeeDAO().update_employee(user_id, employee)
    return {"message": "Employee updated successfully"}

@user_router.delete("/customer/{user_id}")
def delete_customer(user_id: int):
    CustomerDAO().delete_customer(user_id)
    return {"message": "Customer deleted successfully"}

@user_router.delete("/employee/{user_id}")
def delete_employee(user_id: int):
    EmployeeDAO().delete_employee(user_id)
    return {"message": "Employee deleted successfully"}

#create test customer object for me on multiple lines
{
    "password": "password",
    "first_name": "John",
    "last_name": "Doe",
    "birthday": "1990-01-01",
    "profile_pic_URL": "https://www.google.com",
    "age": 30,
    "phone_number": 1234567890,
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

#create test employee object for me on multiple lines
{
    "password": "password",
    "first_name": "John",
    "last_name": "Doe",
    "birthday": "1990-01-01",
    "profile_pic_URL": "https://www.google.com",
    "age": 30,
    "phone_number": 1234567890,
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
            "email": "john.doe@yahoo.com"
        }
    ],
    "ssn": 123456789,
    "salary": 100000,
    "start_date": "2020-01-01",
    "employee_type": "Manager"
}




