from pydantic import BaseModel
from datetime import datetime
from address import Address, AddressCreate, AddressUpdate
from email import Email, EmailCreate, EmailUpdate

# Shared properties
class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: datetime.date
    profile_picture_url: str
    age: int
    address: List[Address]
    email: List[Email]

class Customer(UserBase):
    user_id: int

class CustomerCreate(UserBase):
    pass

class CustomerUpdate(Customer):
    pass

class EmployeeBase(UserBase):
    ssn: int
    salary: int
    start_date: datetime.date
    employee_type: str

class Employee(EmployeeBase):
    user_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(Employee):
    pass






