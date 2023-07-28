from pydantic import BaseModel
from datetime import date
from app.schemas.pydantic.address import Address, AddressCreate, AddressUpdate, AddressBase
from app.schemas.pydantic.email import Email, EmailCreate, EmailUpdate, EmailBase
from typing import List

# Shared properties
class UserBase(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    profile_pic_URL: str
    age: int
    address: List[AddressBase]
    email: List[EmailBase]

class Customer(UserBase):
    user_id: int

class CustomerCreate(UserBase):
    password: str

class CustomerUpdate(Customer):
    pass

class EmployeeBase(UserBase):
    ssn: int
    salary: int
    start_date: date
    employee_type: str

class Employee(EmployeeBase):
    user_id: int

class EmployeeCreate(EmployeeBase):
    password: str

class EmployeeUpdate(Employee):
    pass






